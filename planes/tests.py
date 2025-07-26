

from django.test import TestCase
from .models import Asignatura, PlanEstudio
from .serializers import AsignaturaSerializer, PlanEstudioSerializer

class AsignaturaModelTest(TestCase):
    def setUp(self):
        self.asignatura = Asignatura.objects.create(nombre="Historia", codigo="HIS101", creditos=2)

    def test_creacion_asignatura(self):
        self.assertEqual(self.asignatura.nombre, "Historia")
        self.assertEqual(self.asignatura.codigo, "HIS101")
        self.assertEqual(self.asignatura.creditos, 2)

    def test_str_asignatura(self):
        self.assertEqual(str(self.asignatura), "Historia (HIS101)")

class PlanEstudioModelTest(TestCase):
    def setUp(self):
        self.asignatura = Asignatura.objects.create(nombre="Literatura", codigo="LIT101", creditos=3)
        self.plan = PlanEstudio.objects.create(carrera="Lengua", semestre=1)
        self.plan.asignaturas.add(self.asignatura)

    def test_creacion_plan(self):
        self.assertEqual(self.plan.carrera, "Lengua")
        self.assertEqual(self.plan.semestre, 1)
        self.assertIn(self.asignatura, self.plan.asignaturas.all())

    def test_str_plan(self):
        self.assertEqual(str(self.plan), "Lengua - Semestre 1")

class AsignaturaSerializerTest(TestCase):
    def test_serializer_valido(self):
        data = {
            'nombre': 'Arte',
            'codigo': 'ART101',
            'creditos': 2
        }
        serializer = AsignaturaSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_invalido(self):
        data = {
            'nombre': '',
            'codigo': '',
            'creditos': ''
        }
        serializer = AsignaturaSerializer(data=data)
        self.assertFalse(serializer.is_valid())

class PlanEstudioSerializerTest(TestCase):
    def setUp(self):
        self.asignatura1 = Asignatura.objects.create(nombre="Filosofía", codigo="FIL101", creditos=3)
        self.asignatura2 = Asignatura.objects.create(nombre="Arte", codigo="ART101", creditos=2)

    def test_serializer_valido(self):
        data = {
            'carrera': 'Psicología',
            'semestre': 2,
            'asignaturas': [self.asignatura1.id, self.asignatura2.id]
        }
        serializer = PlanEstudioSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_invalido(self):
        data = {
            'carrera': '',
            'semestre': '',
            'asignaturas': []
        }
        serializer = PlanEstudioSerializer(data=data)
        self.assertFalse(serializer.is_valid())
