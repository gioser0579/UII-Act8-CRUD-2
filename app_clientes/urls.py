# app_clientes/urls.py

from django.urls import path
from . import views  # Importa las vistas de tu app

urlpatterns = [
    # C - Create (Agregar)
    path('agregar/', views.agregar_cliente, name='agregar_cliente'), 
    
    # R - Read (Listar)
    path('', views.listar_clientes, name='listar_clientes'), 
    
    # U - Update (Editar)
    path('editar/<int:pk>/', views.editar_cliente, name='editar_cliente'), 
    
    # D - Delete (Eliminar)
    path('eliminar/<int:pk>/', views.eliminar_cliente, name='eliminar_cliente'), 
]