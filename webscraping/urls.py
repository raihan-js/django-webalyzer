# webscraping/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('analyze/', views.analyze_website, name='analyze_website'),
]
