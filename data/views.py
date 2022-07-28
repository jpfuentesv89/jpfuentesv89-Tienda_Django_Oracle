from urllib import request
from django.shortcuts import render, redirect

from .forms import ClientesForm, iniSesionForm
from .models import Clientes, Compra, detalleCompra, Usuarios, Productos, Pedidos, RegistroSesion

# Create your views here.


def index(request):

    gato = []

    for g in Productos.objects.all():

        if g.idProducto.startswith('G'):

            objgato = Productos.objects.filter(idProducto=g.idProducto)

            gato.append(objgato)

    perro = []

    for p in Productos.objects.all():

        if p.idProducto.startswith('P'):

            objperro = Productos.objects.filter(idProducto=p.idProducto)

            perro.append(objperro)

    datos = {

        'perro': perro, 'gato': gato

    }

    return render(request, './app/index.html', datos)


def perro(request):

    producto = []

    for i in Productos.objects.all():

        if i.idProducto.startswith('P'):

            objproducto = Productos.objects.filter(idProducto=i.idProducto)

            producto.append(objproducto)

    datos = {

        'producto': producto

    }

    return render(request, './app/perro.html', datos)


def gato(request):

    producto = []

    for i in Productos.objects.all():

        if i.idProducto.startswith('G'):

            objproducto = Productos.objects.filter(idProducto=i.idProducto)

            producto.append(objproducto)

    datos = {

        'producto': producto

    }

    return render(request, './app/gato.html', datos)


def sesion(request):

    datos = {

        'form': iniSesionForm()

    }

    if request.method == 'POST':

        formulario = iniSesionForm(request.POST)

        if formulario.is_valid:

            formulario.save()

            datos['mensaje'] = "Sesion registrada exitosamente"

            return redirect ('validaUsuario')

    return render(request, './app/sesion.html', datos)


def nosotros(request):

    return render(request, './app/nosotros.html')


def contactanos(request):

    return render(request, './app/contactanos.html')


def dona(request):

    return render(request, './app/dona.html')


def carrito(request):

    return render(request, './app/carrito.html')


def pagar(request):

    return render(request, './app/pagar.html')


def registrouser(request):

    datos = {

        'form': ClientesForm()

    }

    if request.method == 'POST':

        formulario = ClientesForm(request.POST)

        if formulario.is_valid:

            formulario.save()

            datos['mensaje'] = "Cliente registrado exitosamente"

    return render(request, './app/registrouser.html', datos)


def detallecompra(request, id):

    detalle = detalleCompra.objects.filter(idCompra=id)

    datos = {

        'detalle': detalle

    }

    datos['numeroboleta'] = id

    return render(request, './app/dethistoricompr.html', datos)


def modificaruser(request, id):

    clienteid = Clientes.objects.get(rut=id)

    datos = {

        'form': ClientesForm(instance=clienteid)

    }

    if request.method == 'POST':

        formulario = ClientesForm(data=request.POST, instance=clienteid)

        if formulario.is_valid:

            formulario.save()

            datos['mensaje'] = "Cliente actualizado exitosamente"

    return render(request, './app/modificaruser.html', datos)


def detallepedido(request, id):

    lipiaid = ''

    for i in id:
        if i.isnumeric():
            lipiaid += i

    return redirect('detallecompra', id=lipiaid)


def eliminarVenta(request, id):

    venta = Compra.objects.get(idCompra=id)
    pedido = Pedidos.objects.get(idCompra=id)
    cliente = Clientes.objects.get(rut=venta.rut)
    detventa = detalleCompra.objects.filter(idCompra=id)
    rut = str(cliente.rut)
    pedido.delete()
    detventa.delete()
    venta.delete()
    return redirect('historicompr', id=rut)


def validaUsuario(request):

    contenido = RegistroSesion.objects.all()
    ultimo_inicio = contenido.last()   
    for i in Usuarios.objects.all():
        if i.nombreUser == ultimo_inicio.nombreUser and i.contraseña == ultimo_inicio.contraseña:
            clienteid = Clientes.objects.get(rut=i.rut)
            datos = {

                'usuario': clienteid

            }
            datos['NombreUsuario'] = clienteid.nombre + ' ' + \
                clienteid.apaterno + ' ' + clienteid.amaterno 
            datos['DireccionUser'] = clienteid.direccion
            datos['Comuna'] = clienteid.comuna
            datos['Telefono'] = clienteid.telefono
            return render(request, './app/PerfilUsuario.html', datos)
    return redirect('sesion')


def PerfilUsuario(request):

    return render(request, './app/PerfilUsuario.html')


def historicompr(request, id):

    compra = Compra.objects.filter(rut=id)

    datos = {

        'compra': compra

    }

    return render(request, './app/historicompr.html', datos)


def estadocompra(request, id):

    producto = []
    idCompra = []

    for i in Compra.objects.filter(rut=id):

        objproducto = Pedidos.objects.filter(idCompra=i.idCompra)
        idCompra.append(str(i.idCompra))
        producto.append(objproducto)

    datos = {

        'producto': producto, 'idCompra': idCompra

    }

    return render(request, './app/estadocompra.html', datos)
