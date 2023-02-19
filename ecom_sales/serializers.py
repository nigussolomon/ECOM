from rest_framework import serializers
from .models import SalesOrder, SalesOrderItem, SalesOrderConfirmation
from ecom_store.models import StoreProduct
from ecom_base.serializers import UserSerializer


class CustomProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreProduct
        fields = ['id','product_name','product_image','product_price']

class SalesOrderSerializer(serializers.ModelSerializer):
    customer = UserSerializer()
    class Meta:
        model = SalesOrder
        fields = ['id','customer', 'sales_order_code', 'order_date']

class SalesOrderItemSerializer(serializers.ModelSerializer):
    product = CustomProductSerializer()
    class Meta:
        model = SalesOrderItem
        fields = ['id','sales_order','product', 'quantity', 'delivery_date']

class SalesOrderConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrderConfirmation
        fields = '__all__'