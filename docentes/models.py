
from django.db import models

from planes.models import Asignatura

class Docente(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    correo = models.EmailField(unique=True)
    asignaturas = models.ManyToManyField(Asignatura, related_name="docentes")

    def __str__(self):
        return f"{self.nombre} ({self.cedula})"
