from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import ADMUsuarioForm
from .models import *

class AdminUsuarioForm(admin.ModelAdmin):
    form = ADMUsuarioForm
    list_display = ['usuario', 'password', 'email', 'tipo_usuario', 'is_staff', 'is_active']
admin.site.register(Usuario, AdminUsuarioForm)
admin.site.register(Tipo_Usuario)
admin.site.register(Tipo_Producto)
admin.site.register(Producto)
admin.site.register(Tienda)
admin.site.register(Detalle_Boleta)
admin.site.register(Boleta)