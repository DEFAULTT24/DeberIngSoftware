

from django.test import TestCase, Client
from django.urls import reverse
from estudiantes.models import Estudiante
from datetime import date

class ReporteViewTest(TestCase):
    def setUp(self):
        self.estudiante = Estudiante.objects.create(
            nombre="Prueba",
            apellido="Test",
            cedula="9999999999",
            correo="prueba@test.com",
            fecha_nacimiento=date(2000, 1, 1),
            carrera="Test"
        )

    def test_record_academico_endpoint(self):
        client = Client()
        url = reverse('record-academico', args=[self.estudiante.id])
        response = client.get(url)
        self.assertIn(response.status_code, [200, 403, 401, 404])  # Solo verifica que responde
