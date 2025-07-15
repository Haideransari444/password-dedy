from django.contrib import admin
from django.urls import path
from accounts import views


urlpatterns = [
path("api/auth/register/", views.register_view, name="register"),
path("api/auth/login/", views.login_view, name="login"),
path("api/auth/logout/", views.logout_view, name="logout"),
path("api/auth/profile/", views.user_profile, name="user-profile"),
path("api/auth/stats/", views.user_stats, name="user-stats"),
 path('all/', views.list_all_users, name='list-users')
]
