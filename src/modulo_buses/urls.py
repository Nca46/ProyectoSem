
from django.urls import path
from .views import *

app_name = 'buses'

urlpatterns = [
    path('crear_bus/', ViewCrearBus.as_view(), name='crear_bus'),
    path('editar_bus/<int:pk>/', ViewEditarBus.as_view(), name='editar_bus'),
    path('eliminar_bus/<int:pk>/', ViewEliminarBus.as_view(), name='eliminar_bus'),
    path('ver_bus/', ViewListarBuses.as_view(), name='ver_bus'),

    path('crear_registro/', ViewCrearRegistro.as_view(), name='crear_registro'),
    path('editar_registro/<int:pk>/', ViewEditarRegistro.as_view(), name='editar_registro'),
    path('eliminar_registro/<int:pk>/', ViewEliminarRegistro.as_view(), name='eliminar_registro'),
    path('ver_registro/', ViewListarRegistro.as_view(), name='ver_registro')
]

