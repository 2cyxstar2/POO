from django.contrib import admin

from .models import Empleado


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'sexo', 'puesto', 'departamento', 'estudios')
    search_fields = ('nombre', 'apellido', 'puesto')
