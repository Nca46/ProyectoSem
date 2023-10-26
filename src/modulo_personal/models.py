from django.db import models

# Create your models here.
class personal(models.Model):
    nombres = models.CharField(max_length=256, blank=False, verbose_name='Nombres')
    apellidos = models.CharField(max_length=256, blank=False, verbose_name='Apellidos')
    DPI = models.CharField(max_length=14, unique=True, verbose_name='DPI(CUI)')
    telefono = models.CharField(max_length=8, verbose_name='Telefono')
    correo = models.EmailField(unique=True, verbose_name='Correo')