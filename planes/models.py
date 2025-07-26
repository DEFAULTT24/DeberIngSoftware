from django.db import models

class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    creditos = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"

class PlanEstudio(models.Model):
    carrera = models.CharField(max_length=100)
    semestre = models.PositiveIntegerField()
    asignaturas = models.ManyToManyField(Asignatura, related_name="planes")

    def __str__(self):
        return f"{self.carrera} - Semestre {self.semestre}"
