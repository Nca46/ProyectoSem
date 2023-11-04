from django.views.generic import TemplateView
from django.shortcuts import render
from datetime import datetime
from modulo_registro.models import *
from django.contrib import messages

# Create your views here.

class DashboardView(TemplateView):
    template_name = 'dashboard.html'
    items = Horario.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = self.items
        return context