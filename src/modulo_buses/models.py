from django.db import models
from modulo_personal.models import Personal

desplegable = (
    ('Microbus', 'Microbus'),
    ('Coaster', 'Coaster')
)

class Bus(models.Model):
    tipo_bus = models.CharField(max_length=256, blank=True,choices=desplegable, verbose_name='Tipo de Autobus')
    numero_placa = models.CharField(max_length=256, blank=True, verbose_name='No. de placa')
    codigo_bus = models.CharField(max_length=256,blank=True, verbose_name='Codigo Bus')
    chofer = models.ForeignKey(Personal, on_delete=models.SET_NULL, related_name='buses_chofer', null=True, blank=True, verbose_name='Chofer')
    ayudante = models.ForeignKey(Personal, on_delete=models.SET_NULL, related_name='buses_ayudante', null=True, blank=True, verbose_name='Ayudante')
    horario_salida = models.CharField(max_length=256,blank=True,verbose_name='Horario Salida')
