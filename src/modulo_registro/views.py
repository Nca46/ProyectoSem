from .models import *
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy


# Create your views here.
class ViewListarHorario(ListView):
    model = Horario
    context_object_name = 'hora'
    template_name = 'vista_horario.html'

class ViewCrearHorario(CreateView):
    template_name = 'crear_horario.html'
    model = Horario
    fields = "__all__"
    success_url =reverse_lazy('horario:ver_horario')

class ViewEditarHorario(UpdateView):
    template_name = 'editar_horario.html'
    fields = "__all__"
    model = Horario
    success_url = reverse_lazy('horario:ver_horario')

class ViewEliminarHorario(DeleteView):
    model = Horario
    template_name = 'eliminar_horario.html'
    success_url = reverse_lazy('horario:ver_horario')


class ViewListarRetraso(ListView):
    model = Retraso
    context_object_name = 'retraso'
    template_name = 'vista_retraso.html'

class ViewCrearRetraso(CreateView):
    template_name = 'crear_retraso.html'
    model = Retraso
    fields = "__all__"
    success_url =reverse_lazy('horario:ver_horario')

class ViewEditarRetraso(UpdateView):
    template_name = 'editar_retraso.html'
    fields = "__all__"
    model = Retraso
    success_url = reverse_lazy('horario:ver_horario')

class ViewEliminarRetraso(DeleteView):
    model = Retraso
    template_name = 'eliminar_retraso.html'
    success_url = reverse_lazy('horario:ver_horario')
