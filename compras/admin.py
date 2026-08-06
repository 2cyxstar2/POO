from django.contrib import admin

from .models import Compra


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('folio', 'fecha', 'subtotal', 'iva', 'total', 'proveedor')
    search_fields = ('folio', 'proveedor__razonsocial')
