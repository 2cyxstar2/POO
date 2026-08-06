from django.test import TestCase
from django.urls import reverse

from .models import cliente


class ClienteFormTests(TestCase):
    def test_puede_guardar_un_cliente_y_mostrarlo_en_la_lista(self):
        response = self.client.post(
            reverse('clientes:form-clientes'),
            {
                'nombre': 'Ana',
                'apellido': 'García',
                'sexo': 'Femenino',
                'tipo': 'Regular',
                'direccion': 'Calle 123',
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(cliente.objects.filter(nombre='Ana').exists())

        list_response = self.client.get(reverse('clientes:form-clientes'))
        self.assertContains(list_response, 'Ana')
        self.assertContains(list_response, 'García')
