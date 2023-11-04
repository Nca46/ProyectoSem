
from django.urls import path
from modulo_dashboard.views import  *
app_name = 'dashboard'

urlpatterns = [
    path('', DashboardView.as_view(), name='index'),
]