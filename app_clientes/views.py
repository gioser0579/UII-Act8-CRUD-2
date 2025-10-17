# app_clientes/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente 

# R - Read (Listar Clientes)
def listar_clientes(request):
    clientes = Cliente.objects.all().order_by('apellido', 'nombre')
    return render(request, 'listar_clientes.html', {'clientes': clientes})

# C - Create (Agregar Cliente)
def agregar_cliente(request):
    if request.method == 'POST':
        try:
            Cliente.objects.create(
                nombre=request.POST.get('nombre'),
                apellido=request.POST.get('apellido'),
                telefono=request.POST.get('telefono'),
                correo=request.POST.get('correo'),
                extras_referencias=request.POST.get('extras_referencias')
            )
            return redirect('listar_clientes')
        except Exception as e:
            # Manejo de errores de base de datos (ej. correo duplicado)
            return render(request, 'agregar_cliente.html', {'error': f'Error al guardar: {e}'})
            
    return render(request, 'agregar_cliente.html')

# U - Update (Editar Cliente)
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    
    if request.method == 'POST':
        try:
            cliente.nombre = request.POST.get('nombre')
            cliente.apellido = request.POST.get('apellido')
            cliente.telefono = request.POST.get('telefono')
            cliente.correo = request.POST.get('correo')
            cliente.extras_referencias = request.POST.get('extras_referencias')
            cliente.save()
            return redirect('listar_clientes')
        except Exception as e:
            contexto = {'cliente': cliente, 'error': f'Error al actualizar: {e}'}
            return render(request, 'editar_cliente.html', contexto)
            
    return render(request, 'editar_cliente.html', {'cliente': cliente})

# D - Delete (Eliminar Cliente)
def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    
    if request.method == 'POST':
        cliente.delete()
        return redirect('listar_clientes')
        
    return render(request, 'eliminar_cliente.html', {'cliente': cliente})