from django.urls import path
from django.contrib.auth import views as auth_view
from .views import ProfileCreateView, ProfileUpdateView

app_name = 'auth'

urlpatterns = [
    path('login/', auth_view.LoginView.as_view(), name="login"),
    path('logout/', auth_view.LogoutView.as_view(), name="logout"),

    # I COMMENTED THIS BECAUSE I DO NOT WANT ANYONE TO BE ABLE TO CREATE PROFILE BUT SUPERUSER
    # path('register/', ProfileCreateView.as_view(), name="register"),
    path('update/', ProfileUpdateView.as_view(), name="update"),
]