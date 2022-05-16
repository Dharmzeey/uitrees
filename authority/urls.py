from django.urls import path
from django.contrib.auth import views as auth_view
from .views import ProfileCreateView, ProfileUpdateView

app_name = 'auth'

urlpatterns = [
    path('login/', auth_view.LoginView.as_view(), name="login"),
    path('logout/', auth_view.LogoutView.as_view(), name="logout"),

    path('register', ProfileCreateView.as_view(), name="register"),
    path('update/<int:pk>/', ProfileUpdateView.as_view(), name="update"),
]