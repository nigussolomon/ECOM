from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import EcomProfile, Notification
from .serializers import EcomProfileSerializer, NotificationSerializer
import datetime


class EcomProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        try:
            profile = EcomProfile.objects.get(user=request.user.id)
            serializer = EcomProfileSerializer(profile)
            return Response(
                {"success": True, "data": serializer.data}, status=status.HTTP_200_OK
            )
        except EcomProfile.DoesNotExist:
            return Response(
                {"success": True, "message": "No Profile linked to you user account exists!"}, status=status.HTTP_200_OK
            )


class NotificationHistoryView(APIView):
    permission_classes = [permissions.IsAuthenticated]
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
    permission_classes = [permissions.IsAuthenticated]
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
