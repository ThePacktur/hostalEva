from django.shortcuts import render
from .serializers import HotelSerializer, HabitacionSerializer, PasajeroSerializer, PasajeroHabitacionSerializer
from hotelApp.models import Hotel, Pasajero, Habitacion, PasajeroHabitacion
from rest_framework import viewsets


# Create your views here.
class HotelViewSets(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    
class PasajeroViewSets(viewsets.ModelViewSet):
    queryset = Pasajero.objects.all()
    serializer_class = PasajeroSerializer
    
class HabitacionViewSets(viewsets.ModelViewSet):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer
    
class PasajeroHabitacionViewSets(viewsets.ModelViewSet):
    queryset = PasajeroHabitacion.objects.all()
    serializer_class = PasajeroHabitacionSerializer

