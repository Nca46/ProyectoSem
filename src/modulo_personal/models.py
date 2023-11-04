from django.db import models


rol = (
    ('Ayudante', 'Ayudante'),
    ('Chofer', 'Chofer')
)
# Create your models here.
class Personal(models.Model):
    nombres = models.CharField(max_length=256, blank=True, verbose_name='Nombres')
    apellidos = models.CharField(max_length=256, blank=True, verbose_name='Apellidos')
    DPI = models.CharField(max_length=14, unique=True, verbose_name='DPI(CUI)')
    telefono = models.CharField(max_length=8,unique=True, verbose_name='Telefono')
    correo = models.EmailField(unique=True, verbose_name='Correo')
    rol = models.CharField(max_length=256, blank=True, choices=rol, verbose_name='Rol')

    def __str__(self):
        return f'{self.nombres} {self.apellidos} {self.rol} '