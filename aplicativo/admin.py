from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import *
from .models import *

class AdminUsuarioForm(admin.ModelAdmin):
    form = ADMUsuarioForm
    list_display = ['usuario', 'password', 'email', 'cargo', 'is_staff', 'is_active', 'tienda']
    def cargo(self, obj):
        return obj.tipo_usuario.tipo
class AdminTiendaForm(admin.ModelAdmin):
    form = ADMTiendaForm
    list_display = ['id_tienda', 'nombre', 'direccion', 'encargado']

class AdminProductoForm(admin.ModelAdmin):
    form = ProductoForm
    list_display = ['id_producto', 'nombre', 'descripcion', 'precio_base', 'precio_final', 'tipo_de_producto']
    def tipo_de_producto(self, obj):
        return obj.tipo.tipo
class AdminDetalleForm(admin.ModelAdmin):
    form = DetalleForm
    list_display = ['detalle_id', 'boleta', 'producto', 'cantidad', 'total']
    def boleta(self, obj):
        return obj.id_boleta.id_boleta
    def producto(self, obj):
        return obj.id_producto.nombre

admin.site.register(Usuario, AdminUsuarioForm)
admin.site.register(Tipo_Usuario)
admin.site.register(Oferta)
admin.site.register(Tipo_Producto)
admin.site.register(Producto, AdminProductoForm)
admin.site.register(Tienda, AdminTiendaForm)
admin.site.register(Detalle_Boleta, AdminDetalleForm)
admin.site.register(Boleta)