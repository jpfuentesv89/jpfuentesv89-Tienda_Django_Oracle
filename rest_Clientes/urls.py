from django.urls import path
from rest_Clientes.views import lista_clientes, detalle_clientes
from rest_Clientes.viewslogin import login,register

urlpatterns = [
    path('lista_clientes', lista_clientes, name='lista_clientes'),
    path('detalle_clientes/<id>', detalle_clientes, name='detalle_clientes'),
    path('login', login, name='login'),
    path('register', register, name='register'),
]
