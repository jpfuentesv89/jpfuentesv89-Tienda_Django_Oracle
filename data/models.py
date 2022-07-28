from django.db import models

# Create your models here.
class Comunas(models.Model):
    idComuna = models.IntegerField(primary_key=True,verbose_name='Id de Comuna')
    nombreComuna = models.CharField(max_length=50,verbose_name='Nombre Comuna')

    def __str__(self):
        return self.nombreComuna

class Clientes(models.Model):
    rut = models.IntegerField(primary_key=True,verbose_name='RUT')
    dv = models.CharField(max_length=1,verbose_name='Digito Verificador')
    nombre = models.CharField(max_length=50,verbose_name='Nombre Cliente')
    apaterno = models.CharField(max_length=50,verbose_name='Apellido Paterno')
    amaterno = models.CharField(max_length=50,verbose_name='Apellido Materno')
    direccion = models.CharField(max_length=50,verbose_name='Dirección Cliente')
    comuna = models.ForeignKey(Comunas, on_delete=models.CASCADE)
    correo = models.CharField(max_length=50,verbose_name='Correo Cliente')
    telefono = models.IntegerField(verbose_name='Teléfono')

    def __int__(self):
        return self.rut

class Usuarios(models.Model):
    rut = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    nombreUser = models.CharField(max_length=50,verbose_name='Nombre Usuario')
    contraseña = models.CharField(max_length=50,verbose_name='Contraseña Usuario')

    def __str__(self):
        return self.nombreUser

class RegistroSesion(models.Model):
    nombreUser = models.CharField(max_length=50,verbose_name='Nombre Usuario')
    contraseña = models.CharField(max_length=50,verbose_name='Contraseña Usuario')
    fechainiSesion = models.DateField(auto_now_add=True, verbose_name='Fecha de inicio Sesion')

    def __str__(self):
        return self.nombreUser

class Productos(models.Model):
    idProducto = models.CharField(max_length=5,primary_key=True,verbose_name='ID Producto')
    nombre = models.CharField(max_length=50,verbose_name='Nombre Producto')
    precio = models.IntegerField(verbose_name='Precio Unitario')
    stock = models.IntegerField(verbose_name='Stock de Productos')
    valorizacion = models.CharField(max_length=5,verbose_name='Valorización del Producto')
    descripcion = models.CharField(max_length=50,verbose_name='Descripción del Producto')
    porcentdesc = models.IntegerField(verbose_name='Porcentaje de Descuento')    

    def __str__(self):
        return self.nombre

class Compra(models.Model):
    idCompra = models.IntegerField(primary_key=True,verbose_name='Numero de Compra')
    rut = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    nombreUser = models.CharField(max_length=50,verbose_name='Nombre Usuario')
    Donacion = models.IntegerField(verbose_name='Monto Donado')
    precioNeto = models.IntegerField(verbose_name='Precio Neto Compra')
    precioTotal = models.IntegerField(verbose_name='Precio Total Compra')
    fechaCompra = models.DateField(auto_now_add=True, verbose_name='Fecha de Compra')

    def __int__(self):
        return self.idCompra

class detalleCompra(models.Model):
    idCompra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField(verbose_name='Cantidad Comprada')
    precio = models.IntegerField(verbose_name='Precio Unitario')
    descuento = models.IntegerField(verbose_name='Porcentaje de Descuento')

    def __int__(self):
        return self.idCompra

class Pedidos(models.Model):
    idPedido = models.IntegerField(primary_key=True, verbose_name='Id Pedido')
    fechaPedido = models.DateField(auto_now_add=True, verbose_name='Fecha del Pedido')
    direccionEntrega = models.CharField(max_length=50,verbose_name='Dirección de Entrega')
    comuna = models.ForeignKey(Comunas, on_delete=models.CASCADE)
    estadoEntrega = models.CharField(max_length=50,verbose_name='Estado de la Compra')
    fechaEntrega = models.DateField(auto_now=True, verbose_name='Fecha de Entrega')
    idCompra = models.ForeignKey(Compra, on_delete=models.CASCADE)

    def __int__(self):
        return self.idPedido