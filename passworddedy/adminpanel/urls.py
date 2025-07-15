from django.urls import path
from . import views

urlpatterns = [
    path("stats/", views.platform_stats, name="platform-stats"),
    path("users/", views.manage_users, name="manage-users"),
]
