from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import CustomUser  # Assuming you have a CustomUser model defined in models.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import  UserProfileSerializer
from listings.models import Listing  # for stats
from django.db.models import Sum

@api_view(['POST']) 
def register_view(request): 
    email = request.data.get('email')
    password = request.data.get('password')
    if not email or not password:
        return Response({"error": "Email and password are required."}, status=400)
    if CustomUser.objects.filter(email=email).exists():
        return Response({"error": "Email already exists."}, status=400)
    user = CustomUser.objects.create_user(email=email, password=password)
    return Response({"message": "User created successfully."}, status=201)

@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    if not email or not password:
        return Response({"error": "Email and password are required."}, status=400)
    
    user = authenticate(request, username=email, password=password)
    if user is None:
        return Response({"error": "Invalid credentials."}, status=401)
    
    login(request, user)
    return Response({"message": "Login successful."}, status=200)

@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({"message": "Logout successful."}, status=200)

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = request.user
    if request.method == 'GET':
        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=200)
    
    elif request.method == 'PUT':
        serializer = UserProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_stats(request):
    user = request.user
    listings = user.listings.all()
    active = listings.filter(is_active=True).count()
    lent = listings.filter(status='lent').count()
    earnings = listings.filter(status='lent').aggregate(total=Sum('price'))['total'] or 0

    return Response({
        'active_listings': active,
        'currently_lent': lent,
        'monthly_earnings': earnings,
    })