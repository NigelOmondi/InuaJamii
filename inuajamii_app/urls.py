from django.urls import path
from inuajamii_app import views

urlpatterns = [
    path('', views.home, name='home'),
]