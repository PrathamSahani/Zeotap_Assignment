from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather_summary, name='weather_summary'),
    path('city-weather/', views.city_weather, name='city_weather'), 
]
