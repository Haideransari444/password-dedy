from django.db import models
from django.conf import settings
from listings.models import Listing
from chat.models import Message

class Report(models.Model):
    REPORT_TYPE_CHOICES = [
        ('user', 'User'),
        ('listing', 'Listing'),
        ('message', 'Message'),
    ]

    report_type = models.CharField(max_length=10, choices=REPORT_TYPE_CHOICES)
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reports_made")
    reported_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name="reports_received")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, null=True, blank=True)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, null=True, blank=True)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.report_type.capitalize()} Report by {self.reporter.email}"
