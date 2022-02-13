from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    # path('', views.BaseView.as_view(), name='base'),
    path('', views.HomeView.as_view(), name='home'),
    path('specific-search/<int:pk>/', views.SpecificSearch.as_view(), name='specific-search'),
    path('tree-details/<int:pk>/', views.TreeDetails.as_view(), name='tree-details'),
    path('tree-picture/<int:pk>/', views.TreeLocationPicture.as_view(), name='tree-picture'),

    path('tree-location-details/<int:pk>/', views.TreeLocationDetails.as_view(), name='tree-location-details'),
    path('pharmacological/<int:pk>/', views.Pharmacological.as_view(), name='pharmacology'),

    path('acknowledgement/', views.acknowledgement, name='acknowledgement'),
    path('contributors/', views.TreeContributors.as_view(), name='contributors'),
    path('how-to-use/', views.how_to_use, name='how-to-use'),
    path('about/', views.about, name='about'),
]
