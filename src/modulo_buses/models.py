from django.db import models

desplegable = (
    ('microbus', 'Microbus'),
    ('coaster', 'Coaster')
)

class Bus(models.Model):
    tipo_bus = models.CharField(max_length=256, blank=False,choices=desplegable, verbose_name='Tipo de Autobus')
    numero_placa = models.CharField(max_length=256, blank=False, verbose_name='No. de placa')
    color = models.CharField(max_length=256, blank=False, verbose_name='Color')
    modelo = models.CharField(max_length=256, blank=True, verbose_name='Modelo')
    marca = models.CharField(max_length=256, blank=True, verbose_name='Marca')
    capacidad = models.IntegerField(verbose_name='Capacidad')



