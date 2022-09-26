
from django.urls import path
from Appchoco.views import *

urlpatterns = [
    path('In/',inicio,name="Inicio"),
    path('produc/',producto1,),
    path('contacto/',contacto,name="Contacto"),

    #########leer #####
    path('leerproduc/',leeproductos,name = "productos"),
    path('todomensaje/',todomensajes,name = "todomensaje"),

    ###buscador###
    path('bchoco/',busqueda_chocolate,name ="buscarc"),
    path('buscar/',buscar),
    path('leerchoco/',leeproductos),
    ######formulas###
    path('formu2/',formulari_mens,name="formu2"),    
    path('formu1/',formularioU,name="formu1"),
    path('formu3/',contraseña1,name="formu3"),
    path('formchoco/',chocolateForm),
    
    


    


    
    
    
]
