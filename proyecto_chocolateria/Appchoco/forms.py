from django import forms


class Formulario_usuario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    year = forms.IntegerField()
    fecha = forms.DateField()
    email = forms.EmailField()
class formulario_Productos(forms.Form):
    nombre= forms.CharField()
    fecha = forms.DateField()
    sabor = forms.CharField()