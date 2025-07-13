from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)
class CustomUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = None  # Remove the username field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.email