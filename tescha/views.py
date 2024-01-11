from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Curso, Estudiante, Inscripcion
from .serializer import CursoSerializer, EstudianteSerializer, InscripcionSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class InscripcionViewSet(viewsets.ModelViewSet):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer


def estudianteByMatricula(request, matricula):
    try:
        estudiante = Estudiante.objects.get(matricula=matricula)
        data = {
            'id': estudiante.id,
            'nombre': estudiante.nombre,
            'matricula': estudiante.matricula
        }
        return JsonResponse(data)
    except Estudiante.DoesNotExist:
        return JsonResponse({'error': 'Estudiante no encontrado'}, status=404)