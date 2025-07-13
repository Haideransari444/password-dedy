# notifications/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_notifications),
    path('read/<int:notif_id>/', views.mark_as_read),
]
