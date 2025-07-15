from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from listings.models import Listing
from chat.models import Message, ChatThread
from notifications.models import Notification

User = get_user_model()

def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin)
def platform_stats(request):
    return JsonResponse({
        "total_users": User.objects.count(),
        "total_listings": Listing.objects.count(),
        "total_chats": ChatThread.objects.count(),
        "total_messages": Message.objects.count(),
        "total_notifications": Notifications.objects.count(),
    })

@user_passes_test(is_admin)
def manage_users(request):
    users = User.objects.values("id", "email", "is_active", "date_joined")
    return JsonResponse(list(users), safe=False)
