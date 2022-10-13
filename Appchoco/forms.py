from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Appchoco.models import Avatar, Productos

class formulario_Productos(forms.Form):
    
    nombre= forms.CharField()    
    precio = forms.IntegerField()  
    sabor = forms.CharField()
class formulario_mensaje(forms.Form):
    nombre=forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField()


class formulario_Registro(UserCreationForm):
      
    email = forms.EmailField()    
    password1= forms.CharField(label="Ingrese la contraseña",widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita la contraseña",widget=forms.PasswordInput)
    class Meta:
        model = User
        fields =["username","first_name","last_name","email","password1","password2"]

class formulario_EditarU(UserCreationForm):
    username = forms.CharField(label="Ingrese nombre de usuario nuevo") 
    email = forms.EmailField()     
    password1= forms.CharField(label="Ingrese la contraseña",widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita la contraseña",widget=forms.PasswordInput)
    class Meta:
        model = User
        fields =["username","email","password1","password2"]
        

class Avatarfomulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields =['user','imagen']

class Chocolate_productos(forms.ModelForm):
    class Meta:
        model = Productos
        fields=['nombre','precio','sabor','imagen']
    
