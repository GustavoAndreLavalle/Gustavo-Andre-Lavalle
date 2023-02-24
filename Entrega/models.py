from django.db import models

# Create your models here.

class Estudiante(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    fechaNacimiento = models.DateField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)

class Entregable(models.Model):
    nombre = models.CharField(max_length=40)
    fecha = models.DateField()
    entregado = models.BooleanField()

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    comision = models.IntegerField()
    
