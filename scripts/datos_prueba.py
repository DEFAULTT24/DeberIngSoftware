import os
import django
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion_educativa.settings')
django.setup()

from estudiantes.models import Estudiante
from docentes.models import Docente
from planes.models import Asignatura, PlanEstudio
from calificaciones.models import Calificacion
from matriculas.models import Matricula
from django.contrib.auth.models import User

# Estudiantes
est1 = Estudiante.objects.create(nombre='Juan', apellido='Pérez', cedula='1234567890', correo='juan@email.com', fecha_nacimiento='2000-01-01', carrera='Ingeniería de Software')
est2 = Estudiante.objects.create(nombre='Ana', apellido='García', cedula='0987654321', correo='ana@email.com', fecha_nacimiento='2001-02-02', carrera='Ingeniería Civil')

# Docentes
asig1 = Asignatura.objects.create(nombre='Matemáticas', codigo='MAT101', creditos=4)
asig2 = Asignatura.objects.create(nombre='Programación', codigo='PROG102', creditos=5)
doc1 = Docente.objects.create(nombre='Carlos Ruiz', cedula='111222333', correo='carlos@email.com')
doc1.asignaturas.add(asig1, asig2)
doc2 = Docente.objects.create(nombre='Laura Torres', cedula='444555666', correo='laura@email.com')
doc2.asignaturas.add(asig2)

# Plan de estudio
plan1 = PlanEstudio.objects.create(carrera='Ingeniería de Software', semestre=1)
plan1.asignaturas.add(asig1, asig2)

# Calificaciones
Calificacion.objects.create(estudiante=est1, asignatura=asig1, nota=9.5)
Calificacion.objects.create(estudiante=est1, asignatura=asig2, nota=8.7)
Calificacion.objects.create(estudiante=est2, asignatura=asig1, nota=7.8)

# Matrículas
Matricula.objects.create(estudiante=est1, fecha=datetime.date(2025, 7, 1), valor=1500.00, comprobante='Pago realizado #001')
Matricula.objects.create(estudiante=est2, fecha=datetime.date(2025, 7, 2), valor=1500.00, comprobante='Pago realizado #002')

print('Datos de prueba cargados correctamente.')
