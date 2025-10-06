from django.contrib import admin

# Register your models here.

from .models import Vehiculo
# Registrar el modelo Vehiculo en el admin
admin.site.register(Vehiculo)