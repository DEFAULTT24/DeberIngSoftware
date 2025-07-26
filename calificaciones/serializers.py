
from rest_framework import serializers
from .models import Calificacion
from estudiantes.models import Estudiante
from planes.models import Asignatura

class CalificacionSerializer(serializers.ModelSerializer):
    estudiante = serializers.PrimaryKeyRelatedField(queryset=Estudiante.objects.all())
    asignatura = serializers.PrimaryKeyRelatedField(queryset=Asignatura.objects.all())

    class Meta:
        model = Calificacion
        fields = '__all__'
        extra_kwargs = {
            'estudiante': {'help_text': 'ID del estudiante'},
            'asignatura': {'help_text': 'ID de la asignatura'},
            'nota': {'help_text': 'Nota obtenida'},
        }

    def validate_nota(self, value):
        if value < 0 or value > 10:
            raise serializers.ValidationError("La nota debe estar entre 0 y 10.")
        return value
