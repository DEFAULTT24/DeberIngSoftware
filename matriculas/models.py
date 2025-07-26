
from django.db import models
from estudiantes.models import Estudiante

class Matricula(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name="matriculas")
    fecha = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    comprobante = models.TextField()

    def __str__(self):
        return f"{self.estudiante} - {self.fecha}"
