# listings/utils.py
from notifications.models import Notification

def notify(user, message):
    Notification.objects.create(user=user, message=message)
