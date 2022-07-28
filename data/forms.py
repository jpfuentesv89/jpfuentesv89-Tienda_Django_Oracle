from dataclasses import field, fields
from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import Clientes, RegistroSesion

class ClientesForm(ModelForm):

    class Meta:
        model = Clientes
        fields = ['rut', 'dv', 'nombre', 'apaterno', 'amaterno', 'direccion', 'comuna', 'correo', 'telefono']

class iniSesionForm(ModelForm):

    class Meta:
        model = RegistroSesion
        fields = ['nombreUser', 'contraseña']