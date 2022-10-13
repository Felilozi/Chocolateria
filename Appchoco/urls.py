
from django.urls import path
from Appchoco.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('In/',inicio,name="Inicio"),    
    path('contacto/',contacto,name="Contacto"),

    #########Productos #####
    path('leerproduc/',leeproductos,name = "productos"),
    path('bchoco/',busqueda_chocolate,name ="buscarc"),    
    path('buscar/',buscar), 
    path('chocolates/',chocolateForm,name="Agregar_Choco"),
    path('editarChoco/<nombres>',editarchoco,name="Editar_choco"),
    path('borrarChoco/<nombre1>',productosEli,name="Borrar_choco"),

    ###### Usuario ###
    path('registro/',registrar,name="registro"),
    path('login/',iniciar_sesion1,name="Login"),###Usurio###    
    path('cerrar',LogoutView.as_view(template_name="Appchoco/cerrar.html"),name="Cerrar"),
    path('editarUsuario/',editarU,name="EditarUsu"),
    path('agregarImg/',agregar_imagen,name="AgregarImagen"),

    path('editarImg/<user1>',editarAvatar,name="Editar_Imagen"),
    
    path('modificar/',modificar,name='Modificar'),

 
    

    ###  Usando Class ####    

    path('mensajeC/', MensajeLis.as_view(),name = "LeerMensajes"), ### Leer ###
    path('mensajeC/nuevo', MensajeCrear.as_view(),name ="CrearMensaje"),   ### Crear ### 
    path("mensajeC/<int:pk>",MensajeDetalle.as_view(),name="DetalleMensaje"),### Detalle ###
    path('mensajeC/editar/<int:pk>',MensajeUptade.as_view(),name="EditarMensaje"),### Editar ###
    path('mensajeC/borrar/<int:pk>',Mensajeborrar.as_view(),name="BorrarMensaje"),### Borrar ###
    



 
]
