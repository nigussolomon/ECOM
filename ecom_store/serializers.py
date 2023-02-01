from rest_framework import serializers
from .models import Store, StoreSection
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
    store = StoreSerializerNamePlusCodeOnly()
    class Meta:
        model = StoreSection
        fields = '__all__'