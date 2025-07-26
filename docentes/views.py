from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from drf_yasg.utils import swagger_auto_schema
from .models import Docente
from .serializers import DocenteSerializer

class DocenteViewSet(viewsets.ModelViewSet):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(tags=['Docente'])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Docente'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Docente'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Docente'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Docente'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Docente'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
