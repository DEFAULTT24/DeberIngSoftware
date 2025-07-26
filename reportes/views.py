from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from estudiantes.models import Estudiante
from estudiantes.services import generar_record_academico, calcular_promedio, obtener_comprobante_matricula
from calificaciones.serializers import CalificacionSerializer

class RecordAcademicoView(APIView):
    permission_classes = [IsAuthenticated]
    swagger_tags = ['Reporte']

    def get(self, request, estudiante_id):
        estudiante = Estudiante.objects.get(pk=estudiante_id)
        record = generar_record_academico(estudiante)
        data = CalificacionSerializer(record, many=True).data
        return Response({"estudiante": str(estudiante), "record": data})

class PromedioView(APIView):
    permission_classes = [IsAuthenticated]
    swagger_tags = ['Reporte']

    def get(self, request, estudiante_id):
        estudiante = Estudiante.objects.get(pk=estudiante_id)
        promedio = calcular_promedio(estudiante)
        return Response({"estudiante": str(estudiante), "promedio": promedio})

class ComprobanteMatriculaView(APIView):
    permission_classes = [IsAuthenticated]
    swagger_tags = ['Reporte']

    def get(self, request, estudiante_id):
        estudiante = Estudiante.objects.get(pk=estudiante_id)
        comprobante = obtener_comprobante_matricula(estudiante)
        return Response({"estudiante": str(estudiante), "comprobante": comprobante})
