from django.contrib import admin
from hotelApp.models import Hotel

# Register your models here.
class HotelAdmin(admin.ModelAdmin):
    list_display = ['id','nombreHotel','direccionHotel','numberHotel','habitacionHotel','tarifaHotel','phoneHotel']
    
admin.site.register(Hotel, HotelAdmin)