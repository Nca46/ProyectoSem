from  .models import *
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy

class ViewListarRegistro(ListView):
    model = Registro
    context_object_name = 'registro'
    template_name = 'vista_registro.html'

class ViewCrearRegistro(CreateView):
    template_name = 'crear_registro.html'
    model = Registro
    fields = "__all__"
    success_url =reverse_lazy('dashboard:index')

class ViewEditarRegistro(UpdateView):
    template_name = 'editar_registro.html'
    fields = "__all__"
    model = Registro
    success_url = reverse_lazy('dashboard:index')

class ViewEliminarRegistro(DeleteView):
    model = Registro
    template_name = 'eliminar_registro.html'
    success_url = reverse_lazy('dashboard:index')





class ViewListarBuses(ListView):
    model = Bus
    context_object_name = 'buses'
    template_name = 'vista_bus.html'

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
