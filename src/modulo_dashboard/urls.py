
from django.urls import path
from modulo_dashboard.views import  *
from . import views
app_name = 'dashboard'

urlpatterns = [
    path('', DashboardView.as_view(), name='index'),
    path('guardar_ubicacion/<str:latitud>/<str:longitud>/', views.guardar_ubicacion, name='guardar_ubicacion'),
]