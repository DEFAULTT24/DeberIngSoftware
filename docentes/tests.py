

from django.test import TestCase
from .models import Docente
from .serializers import DocenteSerializer
from planes.models import Asignatura

class DocenteModelTest(TestCase):
    def setUp(self):
        self.asignatura1 = Asignatura.objects.create(nombre="Matemáticas", codigo="MAT101", creditos=4)
        self.asignatura2 = Asignatura.objects.create(nombre="Física", codigo="FIS101", creditos=3)
        self.docente = Docente.objects.create(
            nombre="Ana López",
            cedula="9876543210",
            correo="ana.lopez@example.com"
        )
        self.docente.asignaturas.add(self.asignatura1, self.asignatura2)

    def test_creacion_docente(self):
        self.assertEqual(self.docente.nombre, "Ana López")
        self.assertEqual(self.docente.cedula, "9876543210")
        self.assertEqual(self.docente.correo, "ana.lopez@example.com")

    def test_asignaturas_docente(self):
        asignaturas = self.docente.asignaturas.all()
        self.assertEqual(asignaturas.count(), 2)
        self.assertIn(self.asignatura1, asignaturas)
        self.assertIn(self.asignatura2, asignaturas)

    def test_str_docente(self):
        self.assertEqual(str(self.docente), "Ana López (9876543210)")

class DocenteSerializerTest(TestCase):
    def setUp(self):
        self.asignatura1 = Asignatura.objects.create(nombre="Química", codigo="QUI201", creditos=4)
        self.asignatura2 = Asignatura.objects.create(nombre="Inglés", codigo="ING101", creditos=2)

    def test_serializer_valido(self):
        data = {
            'nombre': 'Mario',
            'cedula': '1231231231',
            'correo': 'mario@example.com',
            'asignaturas': [self.asignatura1.id, self.asignatura2.id]
        }
        serializer = DocenteSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_invalido(self):
        data = {
            'nombre': '',
            'cedula': '',
            'correo': 'noesuncorreo',
            'asignaturas': []
        }
        serializer = DocenteSerializer(data=data)
        self.assertFalse(serializer.is_valid())
