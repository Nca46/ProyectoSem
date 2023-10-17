from  .models import *
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy

class ViewListarTiposBuses(ListView):
    model = TipoBus
    context_object_name = 'tipos_de_buses'
    template_name = 'listar_tipos_bus.html'

# Create your views here.
class ViewCrearTipoBus(CreateView):
    template_name = 'crear_bus.html'
    fields = "__all__"
    model = TipoBus
    success_url = reverse_lazy('dashboard:index')


class ViewEditarTiposBus(UpdateView):
    pass


class ViewEliminarTipoBus(DeleteView):
    pass

