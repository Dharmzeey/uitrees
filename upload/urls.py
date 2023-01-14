from django.urls import path
from . import views

app_name = 'upload'

urlpatterns = [
    path('', views.CreateTree.as_view(), name='upload'),
    path('request/<str:pk>/', views.UploadTreeRequest.as_view(), name='upload_request'),
    path('success', views.Success.as_view(), name='success'),
]


