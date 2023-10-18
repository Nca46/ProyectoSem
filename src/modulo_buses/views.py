from  .models import *
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy

class ViewListarTiposBuses(ListView):
    model = TipoBus
    context_object_name = 'tipos_de_buses'
    template_name = 'listar_tipos_bus.html'

# Create your views here.
class ViewCrearTipoBus(CreateView):
    template_name = 'crear_tipo_bus.html'
    fields = "__all__"
    model = TipoBus
    success_url = reverse_lazy('dashboard:index')


class ViewEditarTiposBus(UpdateView):
    model = TipoBus
    template_name = 'editar_tipo_bus.html'
    fields = "__all__"
    success_url = reverse_lazy('dashboard:index')


class ViewEliminarTipoBus(DeleteView):
    model = TipoBus
    template_name = 'eliminar_tipo_bus.html'
    success_url = reverse_lazy('dashboard:index')

class ViewListarBuses(ListView):
    model = Bus
    context_object_name = 'buses'
    template_name = 'vista_buses.html'

class ViewCrearBus(CreateView):
    template_name = 'crear_bus.html'
    fields = "__all__"
    model = Bus
    success_url =reverse_lazy('dashboard:index')

class ViewEditarBus(CreateView):
    template_name = 'editar_bus.html'
    fields = "__all__"
    model = Bus
    success_url = reverse_lazy('dashboard:index')

class ViewEliminarBus(DeleteView):
    model = Bus
    template_name = 'eliminar_bus.html'
    success_url = reverse_lazy('dashboard:index')
