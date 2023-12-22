from django.db import models

#Source del ManytoMany
#https://www.youtube.com/watch?v=hX8Mcj3-8hk&t=190s
# Create your models here.

class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    nombreHotel = models.CharField(max_length=255, verbose_name='Nombre del hotel')
    direccionHotel = models.CharField(max_length=255, verbose_name='Direccion del hotel', help_text='Ej: Lalo Lala')
    numberHotel = models.IntegerField(verbose_name="Numero de la direccion del hotel", help_text='Ej: 1111')
    habitacionHotel = models.IntegerField(verbose_name='Numero de habitaciones')
    tarifaHotel = models.FloatField(verbose_name='Tarifa del hotel')
    phoneHotel = models.CharField(verbose_name='Numero de telefono del hotel',max_length=15, help_text='Ej: +569787878')
    
    #https://docs.djangoproject.com/en/5.0/ref/models/instances/
    #https://stackoverflow.com/questions/68418311/why-we-use-args-and-kwargs-in-super-save
    #Esta función cambia el formato de Hotel para un resultado más consistente
    def save(self, *args, **kwargs):
        self.nombreHotel = self.nombreHotel.capitalize()
        self.direccionHotel = self.direccionHotel.capitalize()
        super().save(*args, **kwargs)
        
    
    def __str__(self):
        return f'{self.direccionHotel} #{self.numberHotel}'

class Habitacion(models.Model):
    id = models.AutoField(primary_key=True)
    idHotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Dirección del Hotel'
    )
    habitacion = models.CharField(max_length=255, verbose_name='Numero de la habitacion')
    capacidad = models.IntegerField(verbose_name='Capacidad de la habitacion')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio de la habitacion')
    terraza = models.BooleanField(verbose_name='¿Hay terraza?')
    cocina = models.BooleanField(verbose_name='¿Hay cocina?')  
    disponibilidad = models.BooleanField('¿Esta disponible?')
    
    def __str__(self):
        return f'{self.id}{self.idHotel}{self.habitacion}{self.capacidad}{self.precio}{self.terraza}{self.cocina}{self.disponibilidad}'

class Pasajero(models.Model):
    id = models.AutoField(primary_key=True)
    rutClient = models.CharField(max_length=15, verbose_name='Rut', help_text='Ej: 11.111.111-1')
    nombreClient = models.CharField(max_length=255, verbose_name='Nombre', help_text='Eddy')
    apellidoClient = models.CharField(max_length=255, verbose_name='Apellido', help_text='Brock')
    fonoClient = models.CharField(max_length=15, verbose_name='Numero telefonico', help_text='Ej: +569787878')
    email = models.EmailField(max_length=254, verbose_name="Email", help_text='ads@acb.cl')
    fechaNacimiento = models.DateField(null=True, blank=True, verbose_name='Fecha de Nacimiento', help_text='Ej: 1999-10-28')
    
    #Esta función cambia el formato de Pasajero para un resultado más consistente
    def save(self, *args, **kwargs):
        self.rutClient = self.rutClient.upper()
        self.nombreClient = self.nombreClient.capitalize()
        self.apellidoClient = self.apellidoClient.capitalize()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.id}{self.rutClient}{self.nombreClient}{self.apellidoClient}{self.fonoClient}{self.email}{self.fecha_nacimiento}'
    
class PasajeroHabitacion(models.Model):
    id = models.AutoField(primary_key=True)
    pasajero = models.ForeignKey(
        Pasajero,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Nombre del Pasajero'
    )
    habitacion = models.ForeignKey(
        Habitacion,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Numero de habitacion'
    )
    hotel=models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Direccion'
    )
    llegadaClient = models.DateTimeField( verbose_name='Día de llega')
    salidaClient = models.DateTimeField( verbose_name='Dia de salida')
    
    class meta:
        db_table = 'pasajero_pasajero_habitacion'
        verbose_name = "habitacion pasajero"
        verbose_name_plura = 'Habitaciones Pasajeros'
        
    def __str__(self) :
        return f"{self.id}{self.pasajero.id}{self.habitacion.id}{self.hotel.id}{self.llegadaClient}{self.salidaClient}"
    