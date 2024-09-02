from django.urls import path
from .views import get_weather
from .views import create_appointment
from .views import disease_predictor

urlpatterns = [
    path('weather/', get_weather),
    path('create-appointment/', create_appointment),
    path('disease-predictor/', disease_predictor),
]
