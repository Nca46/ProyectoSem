from django.views.generic import TemplateView

# Create your views here.
class ViewIndex(TemplateView):
    template_name = 'dashboard.html'
