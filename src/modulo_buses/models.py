from django.db import models

class TipoBus(models.Model):
    tipo = models.CharField(max_length=256,blank=False)
    capacidad = models.IntegerField(blank=False)
    def __str__(self):
        return self.tipo

class Bus(models.Model):
    placa = models.CharField(max_length=256, blank=False, verbose_name='Numero de placa')
    ultima_fecha_rotacion = models.DateField(blank=False, verbose_name='Ultima fecha de rotación')
    tipo_bus = models.ForeignKey(TipoBus, on_delete=models.PROTECT)

