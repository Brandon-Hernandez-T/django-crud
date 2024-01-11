from django.urls import path, include
from rest_framework import routers
from tescha import views

router = routers.DefaultRouter()
router.register(r'estudiantes', views.EstudianteViewSet, 'estudiantes')
router.register(r'cursos', views.CursoViewSet, 'cursos')
router.register(r'inscripciones', views.InscripcionViewSet, 'inscripciones')

urlpatterns = [
    path('estudiantes/<str:matricula>/', views.estudianteByMatricula, name='estudiante_by_matricula'),
    path('', include(router.urls))
]