from django.urls import path
from users.views import UserRegistrationView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name= 'register'),
]