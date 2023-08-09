from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'first_name', 'last_name', 'email', 'is_active', 'is_staff')
        extra_kwarge = {
            'password' : {
                'write_only' : True,
                'style' : {'input_type' : 'password'}
            }
        }
    
    def create(self, validated_data):
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            password=validated_data['password'],
        )

        return user

class UserPostSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    is_active = serializers.BooleanField(default=True)
    is_staff = serializers.BooleanField(default=False)