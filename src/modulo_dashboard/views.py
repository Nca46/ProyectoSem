from django.views.generic import TemplateView, View
from modulo_registro.models import *
from datetime import date
from django.shortcuts import render, redirect
from .models import Ubicacion
from django.http import JsonResponse

# Create your views here.

def guardar_ubicacion(request, nombre, latitud, longitud):

    try:
        ubicacion = Ubicacion(nombre=nombre, latitud=latitud, longitud=longitud)
        ubicacion.save()
    except Exception as e:
        print(e)

    return redirect('dashboard:index')


class ObtenerUbicaciones(View):

    def get(self, request):
        data = []
        try:
            ubicaciones = Ubicacion.objects.all()
            data = [{"nombre": ubicacion.nombre,
                     "latitud": ubicacion.latitud,
                     "longitud": ubicacion.longitud} for ubicacion in
                                ubicaciones]
        except Exception as e:
            print(e)

        return JsonResponse(data, safe=False)

class DashboardView(TemplateView):
    template_name = 'dashboard.html'
    Ubicacion.objects.all()

    # Obtén la fecha actual
    fecha_actual = date.today()

    # Filtra los retrasos para mostrar solo los de la fecha actual
    retrasos = Retraso.objects.all()
    items = Horario.objects.all()
    paradas = Ubicacion.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = self.items
        context['retrasos'] = self.retrasos
        context['paradas'] = self.paradas
        return context
