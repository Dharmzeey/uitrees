from django.urls import path
from . import views

app_name = 'special'

urlpatterns = [
    path('', views.Special.as_view(), name='special'),
    path('upload/', views.CreateSpecial.as_view(), name='upload'),
    path('details/<int:pk>/', views.SpecialDetails.as_view(), name='details')
]