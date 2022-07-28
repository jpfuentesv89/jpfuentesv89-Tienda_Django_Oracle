from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer


@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)

    username = data['username']
    password = data['password']

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response("Usuario no existe", status=status.HTTP_400_BAD_REQUEST)

    pass_valido = check_password(password, user.password)
    if not pass_valido:
        return Response("Contraseña incorrecta", status=status.HTTP_400_BAD_REQUEST)

    token, created = Token.objects.get_or_create(user=user)

    return Response(token.key)


@api_view(['GET', 'POST', 'PUT'])
def register(request):
    data = JSONParser().parse(request)

    password = data['password']
    is_superuser = '0'
    username = data['username']
    email = data['email']
    is_staff = '0'
    is_active = '1'

    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        if User.objects.filter(username=username).exists():
            return Response("El usuario ya existe", status=status.HTTP_400_BAD_REQUEST)
        else:
            user = User.objects.create_user(username=username, password=password, email=email,
                                            is_superuser=is_superuser, is_staff=is_staff, is_active=is_active)
            user.save()
            return Response("Usuario creado", status=status.HTTP_201_CREATED)
    elif request.method == 'PUT':
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            user.set_password(password)
            user.save()
            return Response("Contraseña actualizada", status=status.HTTP_200_OK)
        else:
            return Response("El usuario no existe", status=status.HTTP_400_BAD_REQUEST)
