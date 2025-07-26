from django.shortcuts import render
from rest_framework import viewsets, permissions
from drf_yasg.utils import swagger_auto_schema
from .models import Calificacion
from .serializers import CalificacionSerializer

class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(tags=['Calificacion'])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Calificacion'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Calificacion'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Calificacion'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Calificacion'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Calificacion'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

# Create your views here.
