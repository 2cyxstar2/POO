from django.contrib import admin
from .models import cliente

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'sexo', 'tipo', 'direccion')
    search_fields = ('apellido', 'sexo')
    list_filter = ('sexo', 'tipo')
    ordering = ('apellido',)
   
admin.site.register(cliente, ClienteAdmin)