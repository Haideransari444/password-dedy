from rest_framework import serializers
from .models import ChatThread, Message
from django.contrib.auth import get_user_model

User = get_user_model()

class UserMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']

class ChatThreadSerializer(serializers.ModelSerializer):
    user1 = UserMiniSerializer(read_only=True)
    user2 = UserMiniSerializer(read_only=True)

    class Meta:
        model = ChatThread
        fields = ['id', 'user1', 'user2', 'created_at', 'is_active']

class MessageSerializer(serializers.ModelSerializer):
    sender = UserMiniSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'thread', 'sender', 'text', 'timestamp', 'is_read']
        read_only_fields = ['sender', 'timestamp', 'is_read']
