from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Listing
from django.urls import path
from .serializers import ListingSerializer
from .utils import notify

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_listing(request):
    serializer = ListingSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save(owner = request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_all_listings(request):
    listings = Listing.objects.filter(is_active=True).order_by('-created_at')
    serializer = ListingSerializer(listings, many=True)
    return Response (serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_listing_status(request,pk):
    try: 
        listing = Listing.objects.get(pk=pk, owner=request.user)
    except Listing.DoesNotExist:
        return Response({'error': 'Listing not found'}, status=status.HTTP_404_NOT_FOUND)
    listing.is_active = not listing.is_active
    listing.save()
    return Response({'status': 'Listing status updated'}, status=status.HTTP_200_OK)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def restore_listing(request, pk):
    try:
        listing = Listing.objects.get(pk=pk, owner=request.user)
    except Listing.DoesNotExist:
        return Response({'error': 'Listing not found'}, status=status.HTTP_404_NOT_FOUND)
    
    listing.is_active = True
    listing.save()
    notify(request.user, f"Your listing '{listing.platform_name}' has been restored.")
    # Notify the user about the change
    return Response({'status': 'Listing restored'}, status=status.HTTP_200_OK)




@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_listing(request, pk):
    try:
        listing = Listing.objects.get(pk=pk, owner=request.user)
    except Listing.DoesNotExist:
        return Response({'error': 'Listing not found'}, status=status.HTTP_404_NOT_FOUND)
    
    listing.delete()
    notify(request.user, f"Your listing '{listing.platform_name}' has been deleted.")
    # Notify the user about the change
    return Response({'status': 'Listing deleted'}, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_listings(request):
    listings = Listing.objects.filter(owner=request.user).order_by('-created_at')
    serializer = ListingSerializer(listings, many=True)
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def mark_listing_as_lent(request, pk):
    try:
        listing = Listing.objects.get(pk=pk, owner=request.user)
    except Listing.DoesNotExist:
        return Response({'error': 'Listing not found'}, status=status.HTTP_404_NOT_FOUND)
    if not listing.is_active:
        return Response({'error': 'Listing is already marked as lent'}, status=status.HTTP_400_BAD_REQUEST)
    
    listing.is_active = False
    listing.status = 'lent'
    listing.save()
    notify(request.user, f"Your listing '{listing.platform_name}' has been marked as lent.")
    # Notify the user about the change
    return Response({'status': 'Listing marked as lent'}, status=status.HTTP_200_OK)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def reactivate_listing(request,pk): 
    try:
        listting = Listing.objects.get(pk=pk, owner=request.user)
    except Listing.DoesNotExist:
        return Response({'error': 'Listing not found'}, status=status.HTTP_404_NOT_FOUND)
    if listting.is_active:
        return Response({'error': 'Listing is already active'}, status=status.HTTP_400_BAD_REQUEST)
    listting.is_active = True
    listting.save()
    notify(request.user, f"Your listing '{listting.platform_name}' has been reactivated.")
    # Notify the user about the change
    return Response({'status': 'Listing reactivated'}, status=status.HTTP_200_OK)
   



@api_view(['GET'])
def search_listing(request):
    q = request.query_params.get('q', '')
    platform = request.query_params.get('platform', '')
    min_price = request.query_params.get('min_price', None)
    max_price = request.query_params.get('max_price', None)
    is_active = request.query_params.get('is_active', None)
    user_id = request.query_params.get('user_id', None)
    listings = Listing.objects.all()
    if q:
        listings = listings.filter(platform_name__icontains=q)
    if platform:
        listings = listings.filter(platform_name__iexact=platform)
    if min_price is not None:
        listings = listings.filter(price__gte=min_price)
    if max_price is not None:
        listings = listings.filter(price__lte=max_price)
    if is_active is not None:
        is_active = is_active.lower() in ['true', '1', 'yes']
        listings = listings.filter(is_active=is_active)
    if user_id is not None:
        listings = listings.filter(owner_id=user_id)
    listings = listings.order_by('-created_at')
    serializer = ListingSerializer(listings, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_listing(request, listing_id):
    try:
        listing = Listing.objects.get(id=listing_id, owner=request.user)
    except Listing.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)

    serializer = ListingSerializer(listing, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)