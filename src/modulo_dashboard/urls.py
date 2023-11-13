
from django.urls import path
from modulo_dashboard.views import  *
from . import views
app_name = 'dashboard'

urlpatterns = [
    path('', DashboardView.as_view(), name='index'),
    path('guardar_ubicacion/<str:nombre>/<str:latitud>/<str:longitud>/', views.guardar_ubicacion, name='guardar_ubicacion'),
    path('obtener_ubicaciones/', views.ObtenerUbicaciones.as_view(), name='obtener_ubicaciones'),

]