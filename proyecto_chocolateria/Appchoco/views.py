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








###########-------Busqueda-----#######################
def busqueda_chocolate(request):
    return render(request,"Appchoco/busquedaC.html")
############----------------Buscar--------------###########    
def buscar(request):
    if request.GET["Nombre"]:
        busqueda = request.GET["Nombre"]
      
        chocolate = Productos.objects.filter(nombre__icontains = busqueda)
        return render(request, "Appchoco/resultado.html",{"chocolate":chocolate,"busqueda":busqueda})
    
    else:
        mensa = "no enviar datos"
    
    return HttpResponse(mensa)



 ###--------Producto--------###   
 #----------Producto 1 ------ #  
def producto(request):
    return render(request,"Appchoco/productos.html")

def chocoNegro(request):
    ipN = 1
    nombreN = "Chocolate Panda"
    fechaN = "2022-09-17"
    saborN = "Chocolate Amargo"
    chocoN = Productos(idP=ipN,nombre = nombreN,fecha = fechaN,sabor = saborN)
    diccionarioNegro = {"nombre_del_producto":nombreN,"fecha":fechaN,"Sabor":saborN}
    plantilla = loader.get_template("Appchoco/chocolate_negro.html")
    documento = plantilla.render(diccionarioNegro)
    chocoN.save()# guardar en la base de datos 
    return HttpResponse(documento)
    
 #----------Producto 2 ------ #  

def chocoSemi(request):
    ipS = 2
    nombreS = "Chocolate Semiamargo "
    fechaS = "2022-09-17"
    saborS = "Chocolate semiamargo"
    chocoS = Productos(idP=ipS ,nombre = nombreS,fecha = fechaS,sabor = saborS)
    diccionarioSemiamargo ={"nombre_del_producto":nombreS,"fecha":fechaS,"Sabor":saborS}
    plantilla = loader.get_template("Appchoco/chocolate_semiamargo.html")
   
    documento = plantilla.render(diccionarioSemiamargo)
    chocoS.save()# guardar en la base de datos 
    return HttpResponse(documento)

 #----------Producto 3 ------ #     

def chocoleche(request):
    ipL = 3
    nombreL = "Chocolate de Leche"
    fechaL = "2022-09-17"
    saborL = "Chocolate de leche"
    chocoL = Productos(idP=ipL,nombre = nombreL,fecha = fechaL,sabor = saborL)
    diccionarioLeche ={"nombre_del_producto":nombreL,"fecha":fechaL,"Sabor":saborL}
    plantilla = loader.get_template("Appchoco/chocolate_leche.html")
    
    documento = plantilla.render(diccionarioLeche)
    chocoL.save()# guardar en la base de datos 
    return HttpResponse(documento)
 #----------Producto 4 ------ #        
def chocoBlanco(request):
    ipB = 4
    nombreB = "Chocolate Blanco"
    fechaB = "2022-09-17"
    saborB = "Chocolate de leche"
    chocoB = Productos(idP =ipB,nombre = nombreB,fecha = fechaB,sabor = saborB)
    diccionarioBlanco = {"nombre_del_producto":nombreB,"fecha":fechaB,"Sabor":saborB}
    plantilla = loader.get_template("Appchoco/chocolate_blanco.html")
    documento = plantilla.render(diccionarioBlanco)
    chocoB.save()# guardar en la base de datos 

    return HttpResponse(documento)   

   

###contacto###
def contacto(request):
    telefonoC  = ("11-000-1251")
    emailC = ("lacuevadelpanda2020@gmail.com") 
    instagramC = "lacuevadelpanda2020"
    #contactoC = Contactos(telefono =telefonoC,email=emailC,instagram = instagramC)
    diccionarioBlanco = {"telefono":telefonoC,"email":emailC,"ig":instagramC}
    plantilla = loader.get_template("Appchoco/contacto.html")
    documento = plantilla.render(diccionarioBlanco)
    #contactoC.save()
    return HttpResponse(documento)   



