from django.urls import path
from .views import fetch_and_save_weather

urlpatterns = [
    path('fetch/', fetch_and_save_weather, name='fetch_and_save_weather'),
]
