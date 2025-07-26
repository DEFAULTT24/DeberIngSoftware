

from django.test import TestCase
from .models import Matricula
from .serializers import MatriculaSerializer
from estudiantes.models import Estudiante
from datetime import date

class MatriculaModelTest(TestCase):
    def setUp(self):
        self.estudiante = Estudiante.objects.create(
            nombre="Lucía",
            apellido="Martínez",
            cedula="5556667778",
            correo="lucia.martinez@example.com",
            fecha_nacimiento=date(2001, 3, 15),
            carrera="Administración"
        )
        self.matricula = Matricula.objects.create(
            estudiante=self.estudiante,
            fecha=date(2025, 7, 1),
            valor=1500.00,
            comprobante="Pago realizado en banco"
        )

    def test_creacion_matricula(self):
        self.assertEqual(self.matricula.estudiante, self.estudiante)
        self.assertEqual(self.matricula.fecha, date(2025, 7, 1))
        self.assertEqual(float(self.matricula.valor), 1500.00)
        self.assertEqual(self.matricula.comprobante, "Pago realizado en banco")

    def test_str_matricula(self):
        esperado = f"{self.estudiante} - 2025-07-01"
        self.assertEqual(str(self.matricula), esperado)

class MatriculaSerializerTest(TestCase):
    def setUp(self):
        self.estudiante = Estudiante.objects.create(
            nombre="Pedro",
            apellido="Sánchez",
            cedula="8889990001",
            correo="pedro.sanchez@example.com",
            fecha_nacimiento=date(2003, 4, 25),
            carrera="Economía"
        )

    def test_serializer_valido(self):
        data = {
            'estudiante': self.estudiante.id,
            'fecha': '2025-08-01',
            'valor': 2000.00,
            'comprobante': 'Pago online'
        }
        serializer = MatriculaSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_invalido(self):
        data = {
            'estudiante': '',
            'fecha': '',
            'valor': '',
            'comprobante': ''
        }
        serializer = MatriculaSerializer(data=data)
        self.assertFalse(serializer.is_valid())
