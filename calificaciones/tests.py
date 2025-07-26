

from django.test import TestCase
from .models import Calificacion
from estudiantes.models import Estudiante
from planes.models import Asignatura
from .serializers import CalificacionSerializer
from datetime import date

class CalificacionModelTest(TestCase):
    def setUp(self):
        self.estudiante = Estudiante.objects.create(
            nombre="Carlos",
            apellido="Gómez",
            cedula="1112223334",
            correo="carlos.gomez@example.com",
            fecha_nacimiento=date(1999, 5, 10),
            carrera="Sistemas"
        )
        self.asignatura = Asignatura.objects.create(nombre="Química", codigo="QUI101", creditos=4)
        self.calificacion = Calificacion.objects.create(
            estudiante=self.estudiante,
            asignatura=self.asignatura,
            nota=8.75
        )

    def test_creacion_calificacion(self):
        self.assertEqual(self.calificacion.estudiante, self.estudiante)
        self.assertEqual(self.calificacion.asignatura, self.asignatura)
        self.assertEqual(float(self.calificacion.nota), 8.75)

    def test_str_calificacion(self):
        esperado = f"{self.estudiante} - {self.asignatura}: 8.75"
        self.assertEqual(str(self.calificacion), esperado)

class CalificacionSerializerTest(TestCase):
    def setUp(self):
        self.estudiante = Estudiante.objects.create(
            nombre="Laura",
            apellido="Ruiz",
            cedula="2223334445",
            correo="laura.ruiz@example.com",
            fecha_nacimiento=date(2002, 2, 20),
            carrera="Contabilidad"
        )
        self.asignatura = Asignatura.objects.create(nombre="Biología", codigo="BIO101", creditos=3)

    def test_serializer_valido(self):
        data = {
            'estudiante': self.estudiante.id,
            'asignatura': self.asignatura.id,
            'nota': 9.5
        }
        serializer = CalificacionSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_invalido(self):
        data = {
            'estudiante': self.estudiante.id,
            'asignatura': self.asignatura.id,
            'nota': 15  # Nota fuera de rango típico
        }
        serializer = CalificacionSerializer(data=data)
        self.assertFalse(serializer.is_valid())
