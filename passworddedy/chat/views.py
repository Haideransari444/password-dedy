from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q

from .models import ChatThread, Message
from .serializers import ChatThreadSerializer, MessageSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatThreadListView(generics.ListAPIView):
    serializer_class = ChatThreadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ChatThread.objects.filter(Q(user1=user) | Q(user2=user))

class StartChatView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        target_id = request.data.get('target_user_id')

        if not target_id:
            return Response({'error': 'target_user_id is required'}, status=400)

        if str(user.id) == str(target_id):
            return Response({'error': 'Cannot start chat with yourself'}, status=400)

        try:
            target_user = User.objects.get(id=target_id)
        except User.DoesNotExist:
            return Response({'error': 'Target user not found'}, status=404)

        # Check for existing thread
        thread = ChatThread.objects.filter(
            (Q(user1=user) & Q(user2=target_user)) |
            (Q(user1=target_user) & Q(user2=user))
        ).first()

        if not thread:
            thread = ChatThread.objects.create(user1=user, user2=target_user)

        serializer = ChatThreadSerializer(thread)
        return Response(serializer.data, status=200)
class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        thread_id = self.kwargs.get('thread_id')
        user = self.request.user

        try:
            thread = ChatThread.objects.get(id=thread_id)
        except ChatThread.DoesNotExist:
            return Message.objects.none()

        if user != thread.user1 and user != thread.user2:
            return Message.objects.none()

        return Message.objects.filter(thread=thread).order_by('timestamp')
class SendMessageView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, thread_id):
        user = request.user
        text = request.data.get('text')

        if not text:
            return Response({'error': 'Text is required'}, status=400)

        try:
            thread = ChatThread.objects.get(id=thread_id)
        except ChatThread.DoesNotExist:
            return Response({'error': 'Thread not found'}, status=404)

        if user != thread.user1 and user != thread.user2:
            return Response({'error': 'Not a participant'}, status=403)

        message = Message.objects.create(thread=thread, sender=user, text=text)
        serializer = MessageSerializer(message)
        return Response(serializer.data, status=201)
