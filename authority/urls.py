from django.urls import path
from django.contrib.auth import views as auth_view
from .views import MyUserCreationView, MyUserUpdateView

app_name = 'auth'

urlpatterns = [
    path('login/', auth_view.LoginView.as_view(), name="login"),
    path('logout/', auth_view.LogoutView.as_view(), name="logout"),

    path('register', MyUserCreationView.as_view(), name="register"),
    path('update/<int:pk>/', MyUserUpdateView.as_view(), name="update"),
]