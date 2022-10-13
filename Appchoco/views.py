from http.client import HTTPResponse
import re
from django.shortcuts import render
from Appchoco.models import *
from Appchoco.forms import *
from django.http import HttpResponse
from django.template import Template,Context,loader
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView, DeleteView 
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout ,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



########------Inicio------######
def inicio(request):

    return render(request,"Appchoco/inicio.html")
@login_required
def modificar(request):
    return render(request,"Appchoco/modificaciones.html")
############# Avatar #############
@login_required
def agregar_imagen(request):
    if request.method=="POST":##boton de subir imagen
        miformulario2 = Avatarfomulario(request.POST, request.FILES)  
        if miformulario2.is_valid():
            informacion= miformulario2.cleaned_data
            avatar=Avatar(user=request.user, imagen=informacion['imagen'])
            avatar.save()
            return render(request,"Appchoco/inicio.html")
    else:
        miformulario2 = Avatarfomulario()
    
    return render(request,"Appchoco/agreImagen.html",{"Miform":miformulario2})    
'''
def editarchoco(request,nombres): #### Editar
    choco = Productos.objects.get(nombre=nombres)
    if request.method=="POST":
        miformulario= Chocolate_productos(request.POST, request.FILES)
        if  miformulario.is_valid(): 
            info= miformulario.cleaned_data

            choco.nombre=info["nombre"]
            choco.precio=info["precio"]
            choco.sabor=info["sabor"]                 
            mi_imagen = info["imagen"]
            if mi_imagen is not None:
                choco.imagen=mi_imagen
            choco.save()

            return render(request,"Appchoco/inicio.html")
    else:
        miformulario = Chocolate_productos(initial={'nombre':choco.nombre,'precio':choco.precio,
       'sabor':choco.sabor,'imagen':choco.imagen}) 
                    
    return render(request,"Appchoco/editarchoco.html",{"choco2":miformulario,'resultado':nombres})



''' 
def editarAvatar(request,user1):
    formulario= Avatar.objects.get(user=user1)
    if request.method=="POST":##boton de subir imagen
        miformulario2 = Avatarfomulario(request.POST, request.FILES)  
        if miformulario2.is_valid():

            informacion= miformulario2.cleaned_data
            
            formulario.user=request.user
            formulario.imagen=informacion['imagen']
            formulario.save()
            return render(request,"Appchoco/inicio.html")
    else:
        miformulario2 = Avatarfomulario()
    
    return render(request,"Appchoco/editarimagen.html",{"Miform1":miformulario2,'resultado':user1})    


#########---Usuario---###############################
def registrar(request):
    if request.method=="POST":
        formU = formulario_Registro(request.POST)
   #      formU= UserCreationForm(request.POST)
        if  formU.is_valid(): #comprobar si no hay errores
            nombreUsuario = formU.cleaned_data["username"]           
            
            formU.save()
            return render(request,"Appchoco/inicio.html",{"men":f"Usuario {nombreUsuario} Creado"})
    else:
        #formU = UserCreationForm()     #mostrar el formulario vacio
        formU = formulario_Registro()
                    
    return render(request,"Appchoco/registro.html",{"formularioUsuario":formU})

###########----Autenticacion --############
def iniciar_sesion1(request):##cambiar el nombre##
    if request.method=="POST":
        form = AuthenticationForm(request,data=request.POST)      #comprobar si no hay errores
        if form.is_valid(): #si el formulario es valido
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user=authenticate(username= usuario,password =contra)
            if user != None :
                login(request, user)
                return render(request, "Appchoco/inicio.html",{"men":f"{user}"})
                
        else: 
            return render(request, "Appchoco/inicio.html",{"men":"Datos incorrecto intentalo nuevamente!!!"})
    else:
        form = AuthenticationForm()
    contexto ={"formPas":form}
    return render(request,"Appchoco/login.html",contexto)


######## ------ Editar usuario ------#####
@login_required
def editarU(request):
    usuarioconectado = request.user
    if request.method=="POST":
        miformulario2= formulario_EditarU(request.POST)
        if  miformulario2.is_valid(): #comprobar si no hay errores

            info= miformulario2.cleaned_data

            usuarioconectado.username= info["username"] #actualizar
            usuarioconectado.email= info["email"]               
            usuarioconectado.password1= info["password1"]
            usuarioconectado.password2= info["password2"]

            usuarioconectado.save()
            return render(request,"Appchoco/inicio.html")
    else:
        miformulario2= formulario_EditarU(initial={"username":usuarioconectado.username,"email":usuarioconectado.email,})
    contexto = {"miformu":miformulario2,"usuario":usuarioconectado}
    return render(request,"Appchoco/editarU.html",contexto)

###########-------Busqueda-----#######################
@login_required
def busqueda_chocolate(request):
    return render(request,"Appchoco/busquedaC.html")
@login_required
def buscar(request):
    if request.GET["Nombre"]:
        busqueda = request.GET["Nombre"]
      
        chocolate = Productos.objects.filter(nombre__icontains = busqueda,)
        return render(request, "Appchoco/resultado.html",{"chocolate":chocolate,"busqueda":busqueda})
    
    else:
        mensa = "no enviar datos"
    return HttpResponse(mensa) 
###################Chocolate#########   
@login_required 
def chocolateForm(request): ###Agregar chocolate
   
    if request.method=="POST":
        choco1= Chocolate_productos(request.POST, request.FILES)
        if  choco1.is_valid(): 
            info= choco1.cleaned_data
            usuario = Productos(
                            nombre=info["nombre"],
                            precio=info["precio"],
                            sabor=info["sabor"],
                            imagen=info["imagen"])
            usuario.save()
            return render(request,"Appchoco/inicio.html")
    else:
        choco1= Chocolate_productos()     
    
                    
    return render(request,"Appchoco/choco.html",{"choco1":choco1})

@login_required 
def leeproductos(request):### Leer chocolate
    productoL = Productos.objects.all()  
    return render(request,"Appchoco/productos.html",{"miproductos":productoL})

@login_required 

def productosEli(request,nombre1): #### Eliminar chocolate
    choco1 = Productos.objects.get(nombre=nombre1)
    choco1.delete()
    choco = Productos.objects.all()  
    return render(request,"Appchoco/inicio.html",{"choco2":choco})

@login_required 
def editarchoco(request,nombres): #### Editar
    choco = Productos.objects.get(nombre=nombres)
    if request.method=="POST":
        miformulario= Chocolate_productos(request.POST, request.FILES)
        if  miformulario.is_valid(): 
            info= miformulario.cleaned_data

            choco.nombre=info["nombre"]
            choco.precio=info["precio"]
            choco.sabor=info["sabor"]                 
            mi_imagen = info["imagen"]
            if mi_imagen is not None:
                choco.imagen=mi_imagen
            choco.save()

            return render(request,"Appchoco/inicio.html")
    else:
        miformulario = Chocolate_productos(initial={'nombre':choco.nombre,'precio':choco.precio,
       'sabor':choco.sabor,'imagen':choco.imagen}) 
                    
    return render(request,"Appchoco/editarchoco.html",{"choco2":miformulario,'resultado':nombres})



###Contacto###

def contacto(request):
    nombrec = ("La cueva del panda ")
    telefonoC  = ("11-000-1251")
    emailC = ("lacuevadelpanda2020@gmail.com") 
    instagramC = "lacuevadelpanda2020"
    diccionarioBlanco = {"nombre":nombrec,"telefono":telefonoC,"email":emailC,"ig":instagramC}
    return render(request,"Appchoco/contacto.html",{"contacto":diccionarioBlanco })
    



############### Class de Mensajes!!! #############

class MensajeLis(ListView): ##Leer
    model = Contactos
  
class MensajeCrear(LoginRequiredMixin,CreateView): #Crear
    model = Contactos
    success_url = "/Appchoco/mensajeC"
    fields= ["nombre","email","mensaje"]

class MensajeDetalle(LoginRequiredMixin,DetailView): #Detalle
    model = Contactos
 
class MensajeUptade(LoginRequiredMixin,UpdateView): #Editar
    model = Contactos
    success_url = "/Appchoco/mensajeC"
    fields= ["nombre","email","mensaje"]
class Mensajeborrar(LoginRequiredMixin,DeleteView): #Borrar
    model = Contactos
    success_url = "/Appchoco/mensajeC"
    fields= ["nombre","email","mensaje"]









