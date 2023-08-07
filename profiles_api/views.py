from django.shortcuts import render
from .models import UserProfile
from .serializers import UserProfileSerializer, UserPostSerializer
from rest_framework.views import Response
from rest_framework import status
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
    
class RegisterView(APIView):
    def post(self, request):
        serializer = UserPostSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            first_name = serializer.validated_data['first_name']
            last_name = serializer.validated_data['last_name']
            try:
                UserProfile.objects.get(email=email)
                return Response({"detail" : "A User with this Email Already exist"}, status=status.HTTP_400_BAD_REQUEST)
            except UserProfile.DoesNotExist:
                user = UserProfile.objects.create_user(email=email, first_name=first_name, last_name=last_name)
                return Response({"detail" : "User Created", "user" : user.email}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)