from django.urls import path, include
from . import views

url_patterns = [
    path('send/', views.sendEmail)
]