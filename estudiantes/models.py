
from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    correo = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()
    carrera = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.cedula})"
