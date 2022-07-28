from django.contrib import admin
from .models import Comunas, Clientes, Usuarios, Productos, Compra, detalleCompra, Pedidos, RegistroSesion
# Register your models here.


admin.site.register(Comunas)
admin.site.register(Clientes)
admin.site.register(Usuarios)
admin.site.register(Productos)
admin.site.register(Compra)
admin.site.register(detalleCompra)
admin.site.register(Pedidos)
admin.site.register(RegistroSesion)