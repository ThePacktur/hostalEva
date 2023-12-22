from rest_framework import serializers
from hotelApp.models import Hotel, Pasajero, Habitacion, PasajeroHabitacion

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class PasajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pasajero
        fields = '__all__'    
        
class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = '__all__'
        
class PasajeroHabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasajeroHabitacion
        fields = '__all__'