from .models import Notification

def send_notification(user, message):
    Notification.objects.create(user=user, message=message)
