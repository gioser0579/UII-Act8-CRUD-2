# app_clientes/admin.py

from django.contrib import admin
from .models import Cliente

# Versión mejorada para ver las columnas importantes en el listado
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'telefono', 'correo', 'id')
    list_filter = ('apellido',)
    search_fields = ('nombre', 'apellido', 'correo')

admin.site.register(Cliente, ClienteAdmin)