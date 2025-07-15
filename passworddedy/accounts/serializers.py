from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'bio', 'avatar', 'is_staff', 'is_active', 'created_at']
        read_only_fields = ['id', 'created_at']  # id and created_at should not be set by the client



User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']
