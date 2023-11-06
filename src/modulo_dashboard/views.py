from django.views.generic import TemplateView
from modulo_registro.models import *
from datetime import date
from django.shortcuts import render, redirect
from .models import Ubicacion
from django.http import JsonResponse

# Create your views here.

def guardar_ubicacion(request, latitud, longitud):
    ubicacion = Ubicacion(latitud=latitud, longitud=longitud)
    ubicacion.save()
    return redirect('dashboard:index')


def obtener_ubicaciones(request):
    ubicaciones = Ubicacion.objects.all()
    ubicaciones_data = [{"latitud": ubicacion.latitud, "longitud": ubicacion.longitud} for ubicacion in ubicaciones]
    return JsonResponse(ubicaciones_data, safe=False)

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    # Obtén la fecha actual
    fecha_actual = date.today()

    # Filtra los retrasos para mostrar solo los de la fecha actual
    retrasos = Retraso.objects.all()
    items = Horario.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = self.items
        context['retrasos'] = self.retrasos
        return context