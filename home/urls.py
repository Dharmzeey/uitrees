from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [

    path('', views.HomeView.as_view(), name='home'),
    path('specific-search/<int:pk>/', views.SpecificSearch.as_view(), name='specific_search'),
    path('tree-details/<str:pk>/', views.TreeDetails.as_view(), name='tree_details'),
    path('tree-picture/<str:pk>/', views.TreeLocationPicture.as_view(), name='tree_picture'),

    path('tree-location-details/<str:pk>/', views.TreeLocationDetails.as_view(), name='tree_location_details'),
    path('pharmacological/<int:pk>/', views.Pharmacological.as_view(), name='pharmacology'),

    path('acknowledgement/', views.acknowledgement, name='acknowledgement'),
    path('contributors/', views.TreeContributor.as_view(), name='contributors'),
    path('tree-album/', views.TreeAlbum.as_view(), name='tree_album'),
    path('how-to-use/', views.how_to_use, name='how_to_use'),
    path('about/', views.about, name='about'),
]
