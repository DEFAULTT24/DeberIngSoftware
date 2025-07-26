
from rest_framework import serializers
from .models import Docente
from planes.models import Asignatura

class DocenteSerializer(serializers.ModelSerializer):
    asignaturas = serializers.PrimaryKeyRelatedField(many=True, queryset=Asignatura.objects.all())

    class Meta:
        model = Docente
        fields = '__all__'
        extra_kwargs = {
            'nombre': {'help_text': 'Nombre del docente'},
            'cedula': {'help_text': 'Cédula única'},
            'correo': {'help_text': 'Correo electrónico'},
            'asignaturas': {'help_text': 'Lista de IDs de asignaturas'},
        }
