from distutils.command.upload import upload
import email
from django.db import models
from django.contrib.auth.models import User


class Productos(models.Model):
    def __str__(self):
        return f"Usuaria {self.nombre}"
    
    nombre= models.CharField(max_length=60)
    precio = models.IntegerField()   
    sabor = models.CharField(max_length=60)
    imagen = models.ImageField(upload_to='images',null=True,blank=True)

class Usuario(models.Model):
    def __str__(self):
        return f"Usuaria {self.nombre} {self.apellido}"
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    fecha = models.DateField()
    year = models.IntegerField()
    email = models.EmailField()



class Contactos(models.Model):
    def __str__(self):
        return f"Contacto {self.nombre} {self.email}"
    nombre = models.CharField(max_length=60)    
    email = models.EmailField()
    mensaje = models.TextField()

class Avatar(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="avatares",null=True,blank=True)