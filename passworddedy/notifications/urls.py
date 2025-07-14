from django.urls import path
from .views import list_notifications, mark_as_read

urlpatterns = [
    path('', list_notifications, name='list-notifications'),
    path('read/<int:notification_id>/', mark_as_read, name='mark-notification-read'),
]
