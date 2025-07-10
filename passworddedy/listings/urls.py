from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_all_listings, name='list_all_listings'),               # GET
    path('create/', views.create_listing, name='create_listing'),              # POST
    path('<int:pk>/status/', views.update_listing_status, name='update_status'),  # PUT
    path('<int:pk>/restore/', views.restore_listing, name='restore_listing'),  # PATCH
    path('<int:pk>/delete/', views.delete_listing, name='delete_listing'),     # DELETE
]
