from django.db import models

# Create your models here.
class Clase (models.Model):
    nombre=models.CharField(max_length=100)
    horario= models.DateField(default=False)
    descripcion=models.TextField()
   
class Estudiante (models.Model):
    nombre=models.CharField(max_length=100)
    correo= models.EmailField(default=False)
    clases_inscritas=models.TextField()   
    
class Profesor (models.Model):
    nombre=models.CharField(max_length=100)
    especialidad= models.TextField(default=False)
    clases_impartidas=models.TextField()
    