from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AsignaturaViewSet, PlanEstudioViewSet

router = DefaultRouter()
router.register(r'asignaturas', AsignaturaViewSet, basename='asignatura')
router.register(r'planes', PlanEstudioViewSet, basename='planestudio')

urlpatterns = [
    path('', include(router.urls)),
]
