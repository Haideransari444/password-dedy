from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_all_listings, name='list_all_listings'),                     # GET (public listings)
    path('create/', views.create_listing, name='create_listing'),                    # POST
    path('my-listings/', views.my_listings, name='my_listings'),                     # GET (user's own listings)
    path('<int:pk>/status/', views.update_listing_status, name='update_status'),     # PUT (toggle is_active)
    path('<int:pk>/delete/', views.delete_listing, name='delete_listing'),           # DELETE
    path('<int:pk>/restore/', views.restore_listing, name='restore_listing'),        # PATCH
    path('<int:pk>/mark-lent/', views.mark_listing_as_lent, name='mark_listing_lent'),  # POST
    path('<int:pk>/reactivate/', views.reactivate_listing, name='reactivate_listing'),  # POST
    path('search/', views.search_listing, name='search_listing'),                    # GET with filters
]
