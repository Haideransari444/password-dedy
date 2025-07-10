from django.contrib import admin
from django.urls import path
from accounts import views


urlpatterns = [
path("api/auth/register/", views.register_view, name="register"),
path("api/auth/login/", views.login_view, name="login"),
path("api/auth/logout/", views.logout_view, name="logout"),
]
