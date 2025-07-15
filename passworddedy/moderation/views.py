from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Report
from .serializers import ReportSerializer

class ReportCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = request.data.copy()
        data['reporter'] = request.user.id
        serializer = ReportSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Report submitted."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
