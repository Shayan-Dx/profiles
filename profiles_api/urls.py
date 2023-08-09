from django.urls import path
from .views import UsersView, DetailView


urlpatterns = [
    path('', UsersView.as_view()),
    path('register/', UsersView.as_view()),
    path('update/<int:primary>/', DetailView.as_view(), name='user-update'),
    path('<int:primary>/', DetailView.as_view()),
]