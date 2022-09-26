import email
from django.db import models



class Productos(models.Model):
    def __str__(self):
        return f"Usuaria {self.nombre},id:{self.idP}"
    idP = models.IntegerField() ###la p es de producto 
    nombre= models.CharField(max_length=60)
    precio = models.IntegerField()   
    sabor = models.CharField(max_length=60)

class Usuario(models.Model):
    def __str__(self):
        return f"Usuaria {self.nombre} {self.apellido}"
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    fecha = models.DateField()
    year = models.IntegerField()
    email = models.EmailField()

class Contraseña(models.Model):
    def __str__(self):
        return f"Usuaria {self.nombre} {self.email}"
    nombre = models.CharField(max_length=60)    
    email = models.EmailField()
    contraseña = models.CharField(max_length=6)

class Contactos(models.Model):
    def __str__(self):
        return f"Contacto{self.nombre} {self.email}"
    nombre = models.CharField(max_length=60)    
    email = models.EmailField()
    mensaje = models.TextField()