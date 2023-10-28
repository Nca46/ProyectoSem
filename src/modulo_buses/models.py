from django.db import models

desplegable = (
    ('microbus', 'Microbus'),
    ('coaster', 'Coaster')
)

ruta = (
    ('coban', 'Coban'),
    ('carcha', 'Carcha')
)

class Bus(models.Model):
    tipo_bus = models.CharField(max_length=256, blank=True,choices=desplegable, verbose_name='Tipo de Autobus')
    numero_placa = models.CharField(max_length=256, default="Sin Placa", blank=False, verbose_name='No. de placa')
    color = models.CharField(max_length=256, default="Sin color",blank=False, verbose_name='Color')
    modelo = models.CharField(max_length=256, blank=True, verbose_name='Modelo')
    marca = models.CharField(max_length=256, blank=True, verbose_name='Marca')
    capacidad = models.IntegerField(default=0,verbose_name='Capacidad')

    def __str__(self):
        return str(self.id)


class Registro(models.Model):
    origen = models.CharField(max_length=256, blank=False,choices=ruta, verbose_name='Origen Bus')
    cantidad_per = models.IntegerField(blank=False, verbose_name='Cantidad de Pasajeros')
    pasaje = models.DecimalField(max_digits=50, decimal_places=3 ,blank=False, verbose_name='Cantidad de Pasaje')
    idBus = models.ForeignKey(Bus, on_delete=models.PROTECT)
    fecha = models.DateTimeField(verbose_name='Fecha')

