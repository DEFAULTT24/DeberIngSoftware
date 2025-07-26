
from rest_framework import serializers
from .models import Estudiante

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'
        extra_kwargs = {
            'nombre': {'help_text': 'Nombre del estudiante'},
            'apellido': {'help_text': 'Apellido del estudiante'},
            'cedula': {'help_text': 'Cédula única'},
            'correo': {'help_text': 'Correo electrónico'},
            'fecha_nacimiento': {'help_text': 'Fecha de nacimiento'},
            'carrera': {'help_text': 'Carrera universitaria'},
        }
