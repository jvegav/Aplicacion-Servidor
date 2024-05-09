from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from cliente import views

urlpatterns = [
    path('verificar/', views.verificar, name='verificar'),
     path('clientes/', views.clientes_list, name = 'clientes_list'),
]