from django.db import models
from django.conf import settings
from django.db import models
# Create your models here.

class Listing(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='listings'
    )
    platform_name  = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
      ('active', 'Active'),
      ('lent', 'Lent')]
    def __str__(self):
        return f"{self.platform_name} - {self.owner.email}"
