from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import SalesOrder, SalesOrderItem, SalesOrderConfirmation
from rest_framework.authentication import TokenAuthentication
from .serializers import SalesOrderSerializer, SalesOrderItemSerializer, SalesOrderConfirmationSerializer
from rest_framework.authtoken.models import Token

# Create your views here.
class SalesOrderView(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.AllowAny]
    def get(self, request, *args, **kwargs):
        user_token = Token.objects.get(key=request.META['HTTP_AUTHORIZATION']).user.id
        try:
            sales_order = SalesOrder.objects.filter(customer=user_token)
            serializer = SalesOrderSerializer(sales_order, many=True)
            return Response(
                {"success": True, "data": serializer.data}, status=status.HTTP_200_OK
            )
        except SalesOrder.DoesNotExist:
            return Response(
                {"success": True, "message": "There is no sales order found!"}, status=status.HTTP_200_OK
            )

class SalesOrderItemView(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.AllowAny]
    def post(self, request, *args, **kwargs):
        print(request)
        try:
            user_token = Token.objects.get(key=request.META['HTTP_AUTHORIZATION']).user.id
            sales_order = SalesOrder.objects.get(id= request.data['sales_order_id'])
            sales_order_item = SalesOrderItem.objects.filter(sales_order= sales_order.id)
            serializer = SalesOrderItemSerializer(sales_order_item, many=True)
            print(request)
            return Response(
                {"success": True, "data": serializer.data}, status=status.HTTP_200_OK
            )
        except SalesOrder.DoesNotExist:
            return Response(
                {"success": True, "message": "There is no sales order item found!"}, status=status.HTTP_200_OK
            )