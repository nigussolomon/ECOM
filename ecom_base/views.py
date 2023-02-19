from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import EcomProfile, Notification
from .serializers import EcomProfileSerializer, NotificationSerializer, RegisterSerializer, UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
import datetime

class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = [permissions.AllowAny]
  serializer_class = RegisterSerializer

class Logout(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        user_token = Token.objects.get(key=request.META['HTTP_AUTHORIZATION']).user
        user_token.auth_token.delete()
        return Response({"success": True, "message": "You have been logged out"},status=status.HTTP_200_OK)


class EcomProfileView(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.AllowAny]
    def get(self, request, *args, **kwargs):
        user_token = Token.objects.get(key=request.META['HTTP_AUTHORIZATION']).user.id
        try:
            user = User.objects.get(id = user_token)
            profile = EcomProfile.objects.get(user=user.id)
            serializer = EcomProfileSerializer(profile)
            return Response(
                {"success": True, "data": serializer.data}, status=status.HTTP_200_OK
            )
        except EcomProfile.DoesNotExist:
            return Response(
                {"success": True, "message": "No Profile linked to you user account exists!"}, status=status.HTTP_200_OK
            )


class NotificationHistoryView(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.AllowAny]
    def get(self, request, *args, **kwargs):
        notification = Notification.objects.filter(
            user=request.user.id, delivery_date__lte=datetime.date.today())
        serializer = NotificationSerializer(notification, many=True)
        if serializer.data != []:
            return Response(
                {"success": True, "data": serializer.data}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"success": True, "message": "No Notification history found for this user account!"}, status=status.HTTP_200_OK
            )


class UnreadNotificationsView(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.AllowAny]
    def get(self, request, *args, **kwargs):
        notification = Notification.objects.filter(
            user=request.user.id, delivery_date__lte=datetime.date.today(), notification_status='unread')
        serializer = NotificationSerializer(notification, many=True)
        if serializer.data != []:
            return Response(
                {"success": True, "data": serializer.data}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"success": True, "message": "No unread notifications found for this user account!"}, status=status.HTTP_200_OK
            )
