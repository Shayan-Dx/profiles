from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'first_name', 'last_name', 'email', 'is_active', 'is_staff')
    

class UserPostSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    is_active = serializers.BooleanField(default=True)
    is_staff = serializers.BooleanField(default=False)