from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from notifications.models import Notifications

User = get_user_model()

class NotificationTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="test@example.com", password="pass1234")
        self.client = APIClient()
        self.client.login(email="test@example.com", password="pass1234")

        # Create a notification for this user
        self.notification = Notifications.objects.create(
            user=self.user,
            message="Test notification",
            is_read=False
        )

    def test_list_notifications(self):
        url = reverse('list-notifications')  # e.g. path('', views.list_notifications, name='list-notifications')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['message'], "Test notification")

    def test_mark_notification_as_read(self):
        url = reverse('mark-as-read', args=[self.notification.id])  # path('read/<int:notification_id>/', ...)
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.notification.refresh_from_db()
        self.assertTrue(self.notification.is_read)

    def test_mark_notification_invalid_user(self):
        other_user = User.objects.create_user(email="hacker@example.com", password="badpass123")
        self.client.logout()
        self.client.login(email="hacker@example.com", password="badpass123")

        url = reverse('mark-as-read', args=[self.notification.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
