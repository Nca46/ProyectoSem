from  .models import *
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy

class ViewListarBuses(ListView):
    model = Bus
    context_object_name = 'buses'
    template_name = 'vista_buses.html'

class ViewCrearBus(CreateView):
    template_name = 'crear_bus.html'
    fields = "__all__"
    model = Bus
    success_url =reverse_lazy('dashboard:index')

class ViewEditarBus(UpdateView):
    template_name = 'editar_bus.html'
    fields = "__all__"
    model = Bus
    success_url = reverse_lazy('dashboard:index')

class ViewEliminarBus(DeleteView):
    model = Bus
    template_name = 'eliminar_bus.html'
    success_url = reverse_lazy('dashboard:index')
