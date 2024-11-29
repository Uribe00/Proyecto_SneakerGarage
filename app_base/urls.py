from django.urls import path, include
from app_base import views

urlpatterns = [
    path('',views.inicio),
]
