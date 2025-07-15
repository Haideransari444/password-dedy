from django.urls import path
from .views import ReportCreateView

urlpatterns = [
    path('', ReportCreateView.as_view(), name='report-create'),
]
