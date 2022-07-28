from django.urls import path
from.views import index, perro, gato, sesion, nosotros, contactanos, dona, carrito, pagar, registrouser, modificaruser, validaUsuario, PerfilUsuario, historicompr, estadocompra, eliminarVenta, detallecompra, detallepedido

urlpatterns = [
    path('', index, name='index'),
    path('perro', perro, name='perro'),
    path('gato', gato, name='gato'),
    path('sesion', sesion, name='sesion'),
    path('nosotros', nosotros, name='nosotros'),
    path('contactanos', contactanos, name='contactanos'),
    path('dona', dona, name='dona'),
    path('carrito', carrito, name='carrito'),
    path('pagar', pagar, name='pagar'),
    path('registrouser', registrouser, name='registrouser'),
    path('modificaruser/<id>', modificaruser, name='modificaruser'),
    path('validaUsuario', validaUsuario, name='validaUsuario'),
    path('PerfilUsuario', PerfilUsuario, name='PerfilUsuario'),
    path('historicompr/<id>', historicompr, name='historicompr'),
    path('estadocompra/<id>', estadocompra, name='estadocompra'),
    path('eliminarVenta/<id>', eliminarVenta, name='eliminarVenta'),
    path('detallecompra/<id>', detallecompra, name='detallecompra'),
    path('detallepedido/<id>', detallepedido, name='detallepedido'),
]