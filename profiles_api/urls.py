from django.urls import path
from .views import AdminUsersView, NormalUsersView, RegisterView


urlpatterns = [
    path('admins/', AdminUsersView.as_view()),
    path('normal/', NormalUsersView.as_view()),
    path('register/', RegisterView.as_view()),
]