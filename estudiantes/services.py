
from calificaciones.models import Calificacion
from matriculas.models import Matricula

def generar_record_academico(estudiante):
    """Devuelve el récord académico del estudiante (asignatura, nota)."""
    return Calificacion.objects.filter(estudiante=estudiante).select_related('asignatura')

def calcular_promedio(estudiante):
    """Calcula el promedio de calificaciones del estudiante."""
    calificaciones = Calificacion.objects.filter(estudiante=estudiante)
    if not calificaciones.exists():
        return 0
    return round(sum([c.nota for c in calificaciones]) / calificaciones.count(), 2)

def obtener_comprobante_matricula(estudiante):
    """Devuelve el comprobante de la última matrícula del estudiante."""
    matricula = Matricula.objects.filter(estudiante=estudiante).order_by('-fecha').first()
    return matricula.comprobante if matricula else None
