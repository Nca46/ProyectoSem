from django.urls import path
from .views import *

app_name = 'personal'

urlpatterns = [
    path('crear_personal/', ViewCrearPersonal.as_view(), name='crear_personal'),
    path('editar_personal/<int:pk>/', ViewEditarPersonal.as_view(), name='editar_personal'),
    path('eliminar_personal/<int:pk>/', ViewEliminarPersonal.as_view(), name='eliminar_personal'),
    path('ver_personal/', ViewListarPersonal.as_view(), name='ver_personal')
]