
from django.urls import path
from .views import *

app_name = 'buses'

urlpatterns = [
    path('crear_tipo/', ViewCrearTipoBus.as_view(), name='crear_tipo_bus'),
    path('editar_tipo/<int:pk>/', ViewEditarTiposBus.as_view(), name='editar_tipo_bus'),
    path('eliminar_tipo/<int:pk>/', ViewEliminarTipoBus.as_view(), name='eliminar_tipo_bus'),
    path('tipos_buses/', ViewListarTiposBuses.as_view(), name='tipos_buses'),

    path('crear_bus/', ViewCrearBus.as_view(), name='crear_bus'),
    path('editar_bus/<int:pk>/', ViewEditarBus.as_view(), name='editar_bus'),
    path('eliminar_bus/<int:pk>/', ViewEliminarBus.as_view(), name='eliminar_bus'),
    path('ver_bus/', ViewListarBuses.as_view(), name='ver_bus')

]

