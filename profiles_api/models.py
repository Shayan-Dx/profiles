from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self, email, first_name, last_name, password=None):
        """Create and saves a user profile"""
        if not email:
            raise ValueError('Users MUST have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        """Create and saves a super user model with the given details"""
        user = self.create_user(email, first_name, last_name, password)

        user.is_superuser = True
        user.is_staff = True
        
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database models for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['name']


    def get_full_name(self):
        """Retrieve full name of the user"""
        return self.first_name
    
    def get_short_name(self):
        """Retrieve short name of the user"""
        return self.last_name
    
    def __str__(self):
        return self.email