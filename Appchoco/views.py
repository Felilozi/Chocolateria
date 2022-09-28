import heapq
from django.shortcuts import render
from re import template
from django.http import HttpResponse
from Appchoco.models import *
from django.template import Template,Context,loader
from Appchoco.forms import *

########------Inicio------######
def inicio(request):
    return render(request,"Appchoco/inicio.html")


#########----Formulario para el usuario---############
def formularioU(request):
    if request.method=="POST":
        formulario1= Formulario_usuario(request.POST)
        if  formulario1.is_valid(): #comprobar si no hay errores
            info= formulario1.cleaned_data
            usuario = Usuario(nombre=info["nombre"],
                            apellido=info["apellido"],
                            year=info["year"],
                            fecha=info["fecha"],
                            email=info["email"])
            usuario.save()
            return render(request,"Appchoco/inicio.html")
    else:
        formulario1= Formulario_usuario()     #mostrar el formulario vacio
    
                    
    return render(request,"Appchoco/form1.html",{"form1":formulario1})


#########----Formulario para el mensaje--############
def formulari_mens(request):
    if request.method=="POST":
        formulario2= formulario_mensaje(request.POST)
        if  formulario2.is_valid(): #comprobar si no hay errores
            info= formulario2.cleaned_data
            usuario2 = Contactos(nombre=info["nombre"],
                            email=info["email"],
                            mensaje=info["mensaje"])
            usuario2.save()
            return render(request,"Appchoco/inicio.html")
    else:
        formulario2= formulario_mensaje()     #mostrar el formulario vacio
    
                    
    return render(request,"Appchoco/form2.html",{"form2":formulario2})


###########----Formulario Contraseña --############
def contraseña1 (request):##cambiar el nombre##
    if request.method=="POST":
        formulario3= Formulario_Contraseña(request.POST)
        if  formulario3.is_valid(): #comprobar si no hay errores
            info= formulario3.cleaned_data
            usuario3 = Contraseña(nombre=info["nombre"],
                            email=info["email"],
                            contraseña=info["contraseña"])
            usuario3.save()
            return render(request,"Appchoco/usuario2.html")
    else:
        formulario3= Formulario_Contraseña()     #mostrar el formulario vacio
    
                    
    return render(request,"Appchoco/form3.html",{"form3":formulario3})

###########-------Busqueda-----#######################
def busqueda_chocolate(request):
    return render(request,"Appchoco/busquedaC.html")
############----------------Buscar--------------###########    
def buscar(request):
    if request.GET["Nombre"]:
        busqueda = request.GET["Nombre"]
      
        chocolate = Productos.objects.filter(nombre__icontains = busqueda,)
        return render(request, "Appchoco/resultado.html",{"chocolate":chocolate,"busqueda":busqueda})
    
    else:
        mensa = "no enviar datos"
    
    return HttpResponse(mensa) 

#######-----Lee los productos --------#####
def leeproductos(request):
    productoslee = Productos.objects.all()
    contexto = {"productos":productoslee}
    return render(request,"Appchoco/productos.html",contexto)



####---Lee los mensajes -----#####  
def todomensajes(request):
    mensajeC = Contactos.objects.all()
    contexto = {"mesaje":mensajeC}
    return render(request,"Appchoco/mensajes.html",contexto)


 ###--------Producto--------#######   

def producto1(request):
    return render(request,"Appchoco/productos.html")
    
 #----------Formulario de choco ------ ####### 
def chocolateForm(request):
   
    if request.method=="POST":
        choco1= formulario_Productos(request.POST)
        if  choco1.is_valid(): 
            info= choco1.cleaned_data
            usuario = Productos(idP=info["idP"],
                            nombre=info["nombre"],
                            precio=info["precio"],
                            sabor=info["sabor"])
            usuario.save()
            return render(request,"Appchoco/inicio.html")
    else:
        choco1= formulario_Productos()     
    
                    
    return render(request,"Appchoco/choco.html",{"choco1":choco1})


###contacto###
def contacto(request):
    nombrec = ("La cueva del panda ")
    telefonoC  = ("11-000-1251")
    emailC = ("lacuevadelpanda2020@gmail.com") 
    instagramC = "lacuevadelpanda2020"
    diccionarioBlanco = {"nombre":nombrec,"telefono":telefonoC,"email":emailC,"ig":instagramC}
    plantilla = loader.get_template("Appchoco/contacto.html")
    documento = plantilla.render(diccionarioBlanco)
    return HttpResponse(documento)   



