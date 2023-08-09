from django.urls import path
from .views import UsersView, RegisterView


urlpatterns = [
    path('', UsersView.as_view()),
    path('register/', RegisterView.as_view()),
]