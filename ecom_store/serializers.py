from rest_framework import serializers
from .models import Store, StoreSection, ProductCategory, StoreProduct
from ecom_base.serializers import UserSerializer


class StoreSerializer(serializers.ModelSerializer):
    store_owner = UserSerializer()

    class Meta:
        model = Store
        fields = '__all__'


class StoreSerializerNamePlusCodeOnly(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ["store_name", "store_code"]


class StoreSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreSection
        fields = '__all__'

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'

class ProductCategory(serializers.ModelSerializer):
    store_section = StoreSectionSerializer()
    class Meta:
        model = StoreProduct
        fields = '__all__'