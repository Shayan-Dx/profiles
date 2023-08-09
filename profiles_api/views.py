from django.shortcuts import render
from .models import UserProfile
from .serializers import UserProfileSerializer, UserPostSerializer
from rest_framework.views import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets


class UsersView(APIView):
    def get(self, request):
        users = UserProfile.objects.all()
        serializer = UserProfileSerializer(users, many=True, context={'request' : request})
        return Response (serializer.data)
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
        

class SearchView(APIView):
    def get(self, request, primary):
        try:
            user = UserProfile.objects.get(pk=primary)
            serializer = UserProfileSerializer(user, context = {'request' : request})
            return Response (serializer.data)
        except UserProfile.DoesNotExist:
            return Response({'detail' : 'There is no user with that user ID!'}, status=status.HTTP_404_NOT_FOUND)


class FeaturesViewSet(viewsets.ViewSet):
    def list(self, request):
        a_viewsets = [
            'Uses actions (list, create, retrieve, update, partial_update)'
            'Automatically maps to URLs using Routers'
            'Provides more functionality with less code'
        ]
        return Response ({'features' : a_viewsets})
