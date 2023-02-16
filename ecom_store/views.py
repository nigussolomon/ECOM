from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Store, StoreSection, ProductCategory
from rest_framework.authentication import TokenAuthentication
from .serializers import StoreSerializer, StoreSectionSerializer, ProductCategorySerializer


class StoreView(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        try:
            store = Store.objects.get(store_owner=request.user.id)
            serializer = StoreSerializer(store)
            return Response(
                {"success": True, "data": serializer.data}, status=status.HTTP_200_OK
            )
        except Store.DoesNotExist:
            return Response(
                {"success": True, "message": "There is no store linked to you user account!"}, status=status.HTTP_200_OK
            )

class StoreSectionView(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        try:
            store = Store.objects.get(store_owner=request.user.id)
            sections = StoreSection.objects.filter(store=store)
            serializer = StoreSectionSerializer(sections, many=True)
            if serializer.data != []:
                return Response(
                    {"success": True, "data": serializer.data}, status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"success": True, "message": "There are no sections to this store!"}, status=status.HTTP_200_OK
                )
        except Store.DoesNotExist:
            return Response(
                {"success": True, "message": "There is no store linked to you user account!"}, status=status.HTTP_200_OK
            )

class ProductCategoryView(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.AllowAny]
    
    def get(self, request, *args, **kwargs):
        categories = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(categories, many=True)
        return Response(
            {"success": True, "data": serializer.data}, status=status.HTTP_200_OK
        )