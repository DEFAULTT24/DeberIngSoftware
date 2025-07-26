from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from drf_yasg.utils import swagger_auto_schema
from .models import Asignatura, PlanEstudio
from .serializers import AsignaturaSerializer, PlanEstudioSerializer

class AsignaturaViewSet(viewsets.ModelViewSet):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(tags=['Asignatura'])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Asignatura'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Asignatura'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Asignatura'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Asignatura'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Asignatura'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class PlanEstudioViewSet(viewsets.ModelViewSet):
    queryset = PlanEstudio.objects.all()
    serializer_class = PlanEstudioSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(tags=['PlanEstudio'])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=['PlanEstudio'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=['PlanEstudio'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=['PlanEstudio'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['PlanEstudio'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['PlanEstudio'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
