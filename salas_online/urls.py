from django.urls import path
from .views import control , pantalla

urlpatterns = [
    path('control/', control, name='control'),
    path('pantalla/', pantalla, name='pantalla'),
]
