from django.contrib import admin
from .models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'categoria', 'color')
    search_fields = ('nombre', 'marca', 'categoria')
