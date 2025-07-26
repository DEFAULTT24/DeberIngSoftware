

from django.test import TestCase
from .models import Estudiante
from .serializers import EstudianteSerializer
from datetime import date

class EstudianteModelTest(TestCase):
    def setUp(self):
        self.estudiante = Estudiante.objects.create(
            nombre="Juan",
            apellido="Pérez",
            cedula="1234567890",
            correo="juan.perez@example.com",
            fecha_nacimiento=date(2000, 1, 1),
            carrera="Ingeniería"
        )

    def test_creacion_estudiante(self):
        self.assertEqual(self.estudiante.nombre, "Juan")
        self.assertEqual(self.estudiante.apellido, "Pérez")
        self.assertEqual(self.estudiante.cedula, "1234567890")
        self.assertEqual(self.estudiante.correo, "juan.perez@example.com")
        self.assertEqual(self.estudiante.fecha_nacimiento, date(2000, 1, 1))
        self.assertEqual(self.estudiante.carrera, "Ingeniería")

    def test_str_estudiante(self):
        self.assertEqual(str(self.estudiante), "Juan Pérez (1234567890)")

class EstudianteSerializerTest(TestCase):
    def test_serializer_valido(self):
        data = {
            'nombre': 'Pedro',
            'apellido': 'López',
            'cedula': '5555555555',
            'correo': 'pedro.lopez@example.com',
            'fecha_nacimiento': '2001-05-10',
            'carrera': 'Derecho'
        }
        serializer = EstudianteSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_invalido(self):
        data = {
            'nombre': '',  # Nombre vacío
            'apellido': 'López',
            'cedula': '',  # Cédula vacía
            'correo': 'noesuncorreo',  # Correo inválido
            'fecha_nacimiento': '',
            'carrera': 'Derecho'
        }
        serializer = EstudianteSerializer(data=data)
        self.assertFalse(serializer.is_valid())
