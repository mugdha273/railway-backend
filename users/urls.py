from django.urls import path
from users.views import UserRegistrationView
from users import views

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name= 'register'),
    # path("", views.index, name="index"),
]