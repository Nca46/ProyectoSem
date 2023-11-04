from django.views.generic import TemplateView
from modulo_registro.models import *
from datetime import date
from django.shortcuts import render, redirect
from .models import Ubicacion
# Create your views here.

def guardar_ubicacion(request, latitud, longitud):
    ubicacion = Ubicacion(latitud=latitud, longitud=longitud)
    ubicacion.save()
    return redirect('dashboard:index')


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
        context['ubicaciones'] = Ubicacion.objects.all()
        return context