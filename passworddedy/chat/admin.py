from django.contrib import admin
from .models import ChatThread, Message

admin.site.register(ChatThread)
admin.site.register(Message)