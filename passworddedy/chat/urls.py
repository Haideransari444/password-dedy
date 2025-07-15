from django.urls import path
from .views import (
    ChatThreadListView, StartChatView,
    MessageListView, SendMessageView
)

urlpatterns = [
    path('threads/', ChatThreadListView.as_view(), name='chat-threads'),
    path('start/', StartChatView.as_view(), name='chat-start'),
    path('thread/<int:thread_id>/messages/', MessageListView.as_view(), name='chat-messages'),
    path('thread/<int:thread_id>/send/', SendMessageView.as_view(), name='chat-send'),
]
