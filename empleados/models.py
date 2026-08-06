from django.db import models


class Empleado(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    sexo = models.CharField(max_length=10)
    puesto = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    estudios = models.CharField(max_length=100)

class nomina(models.Model):
    numperiodo = models.CharField(max_length=20)
    fecha = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    percepciones = models.DecimalField(max_digits=10, decimal_places=2)
    deducciones = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='nominas')

    def __str__(self):
        return self.numperiodo
