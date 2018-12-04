from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import *
from .models import *

class AdminUsuarioForm(admin.ModelAdmin):
    form = ADMUsuarioForm
    list_display = ['usuario', 'password', 'email', 'tipo_usuario', 'is_staff', 'is_active']

class AdminTiendaForm(admin.ModelAdmin):
    form = TiendaForm
    list_display = ['id_tienda', 'nombre', 'direccion']

admin.site.register(Usuario, AdminUsuarioForm)
admin.site.register(Tipo_Usuario)
admin.site.register(Tipo_Producto)
admin.site.register(Producto)
admin.site.register(Tienda, AdminTiendaForm)
admin.site.register(Detalle_Boleta)
admin.site.register(Boleta)