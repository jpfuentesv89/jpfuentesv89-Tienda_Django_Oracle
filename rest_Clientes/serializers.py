from rest_framework import serializers
from data.models import Clientes
from django.contrib.auth.models import User



class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clientes
        fields = ['rut', 'dv', 'nombre', 'apaterno', 'amaterno', 'direccion', 'comuna', 'correo', 'telefono']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['password', 'is_superuser', 'username','email','is_staff','is_active']