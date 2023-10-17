
from django.urls import path
from .views import *

app_name = 'buses'

urlpatterns = [
    path('crear_tipo/', ViewCrearTipoBus.as_view(), name='crear_tipo_bus'),
    path('tipos_buses/', ViewListarTiposBuses.as_view(), name='tipos_buses')
]
