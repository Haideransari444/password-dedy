from rest_framework import serializers
from .models import CustomUser

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'bio', 'avatar', 'is_staff', 'is_active', 'created_at']
        read_only_fields = ['id', 'created_at']  # id and created_at should not be set by the client
