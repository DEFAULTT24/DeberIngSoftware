
from django.db import models
from estudiantes.models import Estudiante
from planes.models import Asignatura

class Calificacion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name="calificaciones")
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, related_name="calificaciones")
    nota = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.estudiante} - {self.asignatura}: {self.nota}"
