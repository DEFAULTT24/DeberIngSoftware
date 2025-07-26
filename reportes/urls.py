from django.urls import path
from .views import RecordAcademicoView, PromedioView, ComprobanteMatriculaView

urlpatterns = [
    path('record/<int:estudiante_id>/', RecordAcademicoView.as_view(), name='record-academico'),
    path('promedio/<int:estudiante_id>/', PromedioView.as_view(), name='promedio-estudiante'),
    path('comprobante/<int:estudiante_id>/', ComprobanteMatriculaView.as_view(), name='comprobante-matricula'),
]
