
from django.urls import path
from Appchoco.views import *

urlpatterns = [
    path('In/',inicio,name="Inicio"),
    path('produc/',producto,name = "productos"),
    path('chocolateN/',chocoNegro,name="chocolateNegro"),
    path('chocolate_semi/',chocoSemi,name="chocolate_semi"),
    path('chocolate_leche/',chocoleche,name="chocolate_leche"),
    path('chocolate_blanco/',chocoBlanco,name="chocolate_blanco"),
    path('contacto/',contacto,name="Contacto"),
    path('formu1/',formularioU,name="formu1"),
    path('bchoco/',busqueda_chocolate,name ="buscarc"),
    path('buscar/',buscar),
    
    


    


    
    
    
]
