from django.urls import path
from .views import UsersView, RegisterView, SearchView


urlpatterns = [
    path('', UsersView.as_view()),
    path('register/', RegisterView.as_view()),
    path('<int:primary>/', SearchView.as_view()),
]