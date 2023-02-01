from rest_framework import serializers
from .models import EcomProfile, Notification
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]

class EcomProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = EcomProfile
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'