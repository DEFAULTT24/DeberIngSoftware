from django.shortcuts import render

from rest_framework import viewsets, permissions
from drf_yasg.utils import swagger_auto_schema
from .models import Matricula
from .serializers import MatriculaSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(tags=['Matricula'])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Matricula'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Matricula'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Matricula'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Matricula'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Matricula'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

# Create your views here.

# Create your views here.
