from django.urls import path
from django.contrib.auth import views as auth_view
from .views import UserCreateView, UserUpdateView

app_name = 'auth'

urlpatterns = [
    path('login/', auth_view.LoginView.as_view(), name="login"),
    path('logout/', auth_view.LogoutView.as_view(), name="logout"),

    # I COMMENTED THIS BECAUSE I DO NOT WANT ANYONE TO BE ABLE TO CREATE User BUT SUPERUSER
    path('register/', UserCreateView.as_view(), name="register"),
    path('update/', UserUpdateView.as_view(), name="update"),
]