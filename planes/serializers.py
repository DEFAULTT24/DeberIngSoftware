
from rest_framework import serializers
from .models import Asignatura, PlanEstudio

class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = '__all__'
        extra_kwargs = {
            'nombre': {'help_text': 'Nombre de la asignatura'},
            'codigo': {'help_text': 'Código único'},
            'creditos': {'help_text': 'Cantidad de créditos'},
        }

class PlanEstudioSerializer(serializers.ModelSerializer):
    asignaturas = serializers.PrimaryKeyRelatedField(many=True, queryset=Asignatura.objects.all())

    class Meta:
        model = PlanEstudio
        fields = '__all__'
        extra_kwargs = {
            'carrera': {'help_text': 'Nombre de la carrera'},
            'semestre': {'help_text': 'Número de semestre'},
            'asignaturas': {'help_text': 'Lista de IDs de asignaturas'},
        }
