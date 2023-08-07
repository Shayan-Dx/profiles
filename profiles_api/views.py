from django.shortcuts import render
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.views import Response
from rest_framework.views import APIView


class AdminUsersView(APIView):
    def get(self, request):
        users = UserProfile.objects.filter(is_staff=True, is_active=True)
        serializer = UserProfileSerializer(users, many=True, context={'request' : request})
        return Response (serializer.data)
    
class NormalUsersView(APIView):
    def get(self, request):
        users = UserProfile.objects.filter(is_staff=False, is_active=True)
        serializer = UserProfileSerializer(users, many=True, context={'request' : request})
        return Response (serializer.data)