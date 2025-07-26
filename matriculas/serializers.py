
from rest_framework import serializers
from .models import Matricula
from estudiantes.models import Estudiante

class MatriculaSerializer(serializers.ModelSerializer):
    estudiante = serializers.PrimaryKeyRelatedField(queryset=Estudiante.objects.all())

    class Meta:
        model = Matricula
        fields = '__all__'
        extra_kwargs = {
            'estudiante': {'help_text': 'ID del estudiante'},
            'fecha': {'help_text': 'Fecha de matrícula'},
            'valor': {'help_text': 'Valor de la matrícula'},
            'comprobante': {'help_text': 'Comprobante de pago (texto o archivo codificado)'},
        }
