from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from data.models import Clientes
from .serializers import ClienteSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def lista_clientes(request):
    """
    Lista todos los clientes, o crea un nuevo cliente
    """
    if request.method == 'GET':
        clientes = Clientes.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        if Clientes.objects.filter(rut=request.data['rut']).exists():
            return Response("El cliente ya existe", status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = ClienteSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("El cliente fue creado", status=status.HTTP_201_CREATED)
            return Response("El cliente no pudo ser creado", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_clientes(request, id):
    """
    Retorna, actualiza o elimina un cliente
    """
    try:
        cliente = Clientes.objects.get(rut=id)
    except Clientes.DoesNotExist:
        return Response("El cliente no existe", status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClienteSerializer(cliente)
        return Response("El cliente fue encontrado", status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ClienteSerializer(cliente, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response("El cliente fue actualizado", status=status.HTTP_200_OK)
        return Response("El cliente no pudo ser actualizado", status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cliente.delete()
        return Response("El cliente fue eliminado", status=status.HTTP_204_NO_CONTENT)
