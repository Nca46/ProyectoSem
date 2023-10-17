from django.urls import path
from .views import *

app_name = 'dashboard'

urlpatterns = [
    path('', ViewIndex.as_view(), name='index'),
]
