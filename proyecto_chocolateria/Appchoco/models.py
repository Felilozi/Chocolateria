import email
from django.db import models



class Productos(models.Model):
    idP = models.IntegerField() ###la p es de producto 
    nombre= models.CharField(max_length=60)
    fecha = models.DateField()
    sabor = models.CharField(max_length=60)

class Usuario(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    year = models.IntegerField()
    fecha = models.DateField()
    email = models.EmailField()

class Contactos(models.Model):
    telefono = models.CharField(max_length=10)
    email = models.EmailField()
    instagram = models.CharField(max_length=60)

