from .models import *
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy


# Create your views here.
class ViewListarPersonal(ListView):
    model = personal
    context_object_name = 'persona'
    template_name = 'vista_personal.html'

class ViewCrearPersonal(CreateView):
    template_name = 'crear_personal.html'
    model = personal
    fields = "__all__"
    success_url =reverse_lazy('dashboard:index')

class ViewEditarPersonal(UpdateView):
    template_name = 'editar_personal.html'
    fields = "__all__"
    model = personal
    success_url = reverse_lazy('dashboard:index')

class ViewEliminarPersonal(DeleteView):
    model = personal
    template_name = 'eliminar_personal.html'
    success_url = reverse_lazy('dashboard:index')