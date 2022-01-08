from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('specific-search/<int:pk>/', views.SpecificSearch.as_view(), name='specific-search'),
    path('tree-details/<int:pk>/', views.TreeDetails.as_view(), name='tree-details'),
    path('tree-picture/<int:pk>/', views.TreeLocationPicture.as_view(), name='tree-picture'),

    path('tree-location-details/<int:pk>/', views.TreeLocationDetails.as_view(), name='tree-location-details'),
    path('pharmacological/<int:pk>/', views.Pharmacological.as_view(), name='pharmacology'),

    path('steal', views.Steal.as_view(), name="steal")
]

