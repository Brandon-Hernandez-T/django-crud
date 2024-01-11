from django.db import models
from django.contrib.auth.models import User

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    matricula = models.CharField(max_length=100)

    def __str__(self):
        return self.matricula
    
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    creditos = models.PositiveIntegerField()
    horario = models.CharField(max_length=50)
    cupo = models.PositiveIntegerField()
    maestro = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='curso_images/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    cruso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
