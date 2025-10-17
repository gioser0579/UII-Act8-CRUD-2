# app_clientes/models.py

from django.db import models

class Cliente(models.Model):
    # id_cliente lo crea Django automáticamente como 'id'
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, blank=True, null=True) # El teléfono puede no ser obligatorio
    correo = models.EmailField(max_length=254, unique=True) # El correo debe ser único
    # Renombramos 'extras/referencias' a un campo de texto
    extras_referencias = models.TextField(blank=True) 

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name_plural = "Clientes"