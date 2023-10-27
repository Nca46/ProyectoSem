from django.urls import path
from .views import *

app_name = 'horario'

urlpatterns = [
    path('crear_horario/', ViewCrearHorario.as_view(), name='crear_horario'),
    path('editar_horario/<int:pk>/', ViewEditarHorario.as_view(), name='editar_horario'),
    path('eliminar_horario/<int:pk>/', ViewEliminarHorario.as_view(), name='eliminar_horario'),
    path('ver_horario/', ViewListarHorario.as_view(), name='ver_horario'),

    path('crear_retraso/', ViewCrearRetraso.as_view(), name='crear_retraso'),
    path('editar_retraso/<int:pk>/', ViewEditarRetraso.as_view(), name='editar_retraso'),
    path('eliminar_retraso/<int:pk>/', ViewEliminarRetraso.as_view(), name='eliminar_retraso'),
    path('ver_retraso/', ViewListarRetraso.as_view(), name='ver_retraso')
]