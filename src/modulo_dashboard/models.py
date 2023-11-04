from django.db import models

class Ubicacion(models.Model):
    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Ubicación: Latitud {self.latitud}, Longitud {self.longitud}'