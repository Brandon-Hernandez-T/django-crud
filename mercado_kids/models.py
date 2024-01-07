from django.db import models

class ClientePapa(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    rfc = models.CharField(max_length=50)
    numero_telefono = models.CharField(max_length=20)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre
    
class ClienteNino(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    cumple = models.DateField()
    cliente_papa = models.ForeignKey(ClientePapa, on_delete=models.CASCADE, related_name='hijos')

    def __str__(self):
        return self.nombre
