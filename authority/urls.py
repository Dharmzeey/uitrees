from django.urls import path
from . import views

app_name = 'authority'

urlpatterns = [
    path('login/', views.CustomLogin.as_view(), name='login')
]