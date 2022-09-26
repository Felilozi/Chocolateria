from django import forms



class Formulario_usuario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    year = forms.IntegerField()
    fecha = forms.DateField()
    email = forms.EmailField()
class formulario_Productos(forms.Form):
    idP= forms.IntegerField() 
    nombre= forms.CharField()    
    precio = forms.IntegerField()  
    sabor = forms.CharField()
class formulario_mensaje(forms.Form):
    nombre=forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField()
class Formulario_Contraseña(forms.Form):
    email = forms.EmailField()
    nombre = forms.CharField()
    contraseña= forms.CharField(widget = forms.PasswordInput())
        