from django.db import models

from productos.models import Producto
from proveedores.models import Proveedor


class Compra(models.Model):
    folio = models.CharField(max_length=20)
    fecha = models.DateField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='compras')

    def __str__(self):
        return f'Compra {self.folio}'
