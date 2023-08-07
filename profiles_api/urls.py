from django.urls import path
from .views import AdminUsersView, NormalUsersView


urlpatterns = [
    path('admins/', AdminUsersView.as_view()),
    path('normal/', NormalUsersView.as_view()),
]