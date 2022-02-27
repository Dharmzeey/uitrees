from django.urls import path

from . import views

app_name = 'treerequest'

urlpatterns = [
    path('', views.RequestTreeView.as_view(), name='treerequest')
]