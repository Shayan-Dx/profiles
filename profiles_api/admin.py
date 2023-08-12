from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin


@admin.register(UserProfile)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'password', 'first_name', 'last_name', 'is_active', 'is_staff')