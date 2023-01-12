from django.urls import path

from . import views

app_name = 'treerequest'

urlpatterns = [
    path('', views.RequestTreeView.as_view(), name='treerequest'),
    path('requests/', views.ViewRequest.as_view(), name='requests'),
    path('<str:pk>/request-details/', views.RequestDetails.as_view(), name='request_details'),
]