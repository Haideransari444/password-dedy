from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import CustomUser  # Assuming you have a CustomUser model defined in models.py

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

