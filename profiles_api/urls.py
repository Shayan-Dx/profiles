from django.urls import path
from .views import UsersView, SearchView


urlpatterns = [
    path('', UsersView.as_view()),
    path('register/', UsersView.as_view()),
    path('<int:primary>/', SearchView.as_view()),
]