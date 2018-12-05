from django import forms
from django.contrib import admin
from .models import *

class LoginForm(forms.Form):
    usuario = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'class': 'form-control cortoCentrado', 'placeholder':'Usuario', 'name':'usuario'}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control cortoCentrado', 'placeholder': 'Contraseña', 'name':'contraseña'}))

class AsignarTienda(forms.Form):
    sujeto = forms.ModelChoiceField(queryset=Usuario.objects.all(), widget=forms.Select(attrs={'class':'form-control cortoCentrado'}))
    tienda = forms.ModelChoiceField(queryset=Tienda.objects.all(), widget=forms.Select(attrs={'class':'form-control cortoCentrado'}))

    def __init__(self, *args, **kwargs):
        super(AsignarTienda, self).__init__(*args, **kwargs)
        self.fields['tienda'].label_from_instance = lambda obj: "%s - %s" % (obj.id_tienda, obj.nombre)

    def Guardar(self, user, tiend):
        usr = Usuario.objects.get(usuario=user)
        usr.tienda = Tienda.objects.get(id_tienda=tiend)
        usr.save()
        return True

class RegistroForm(forms.ModelForm):
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control cortoCentrado', 'placeholder': 'Contraseña', 'name':'contraseña'}))
    class Meta:
        model = Usuario
        fields = ('usuario', 'email', 'tienda')
        widgets = {
            'usuario': forms.TextInput(attrs={'class':'form-control cortoCentrado', 'placeholder':'Usuario', 'onkeypress':'return validarCorreo(event)'}),
            'email': forms.EmailInput(attrs={'class':'form-control cortoCentrado', 'placeholder':'Correo Electrónico', 'onkeypress':'return validarCorreo(event)'}),
            'tienda': forms.Select(attrs={'class':'form-control cortoCentrado'}),
        }
    def __init__(self, *args, **kwargs):
        super(RegistroForm, self).__init__(*args, **kwargs)
        self.fields['tienda'].queryset = Tienda.objects.all()
        self.fields['tienda'].label_from_instance = lambda obj: "%s - %s" % (obj.id_tienda, obj.nombre)
        self.fields['password'].label = 'Contraseña'
        self.fields['email'].label = 'Correo electrónico'

class ADMUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        exclude = ['is_staff', 'is_superuser']

#Forms para la web.

class ADMTiendaForm(forms.ModelForm):
    encargado = forms.ModelChoiceField(queryset=Usuario.objects.filter(tipo_usuario__in=Tipo_Usuario.objects.filter(id_tipo=2)), widget=forms.Select(attrs={'class':'form-control cortoCentrado'}))
    class Meta:
        model = Tienda
        exclude = ['id_tienda']
        widgets = {
            'nombre': forms.TextInput(attrs={'maxlength':'20', 'class':'form-control cortoCentrado', 'placeholder':'Nombre de la Sucursal','onkeypress':'return validarNombre(event, this)'}),
            'direccion': forms.TextInput(attrs={'maxlength':'100','class':'form-control cortoCentrado', 'placeholder':'Dirección'}),
            'ciudad': forms.TextInput(attrs={'class':'form-control cortoCentrado'}),
            'comuna': forms.TextInput(attrs={'class':'form-control cortoCentrado'}),
            'telefono': forms.NumberInput(attrs={'class':'form-control cortoCentrado', 'onkeypress':'return validarNumero(event, this)'}),
            'correo': forms.EmailInput(attrs={'class':'form-control cortoCentrado', 'placeholder':'Correo', 'onkeypress':'return validarCorreo(event)'}),
        }

class TiendaForm(forms.ModelForm):
    encargado = forms.ModelChoiceField(queryset=Usuario.objects.filter(tipo_usuario__in=Tipo_Usuario.objects.filter(id_tipo=2)), widget=forms.Select(attrs={'class':'form-control cortoCentrado'}))
    class Meta:
        model = Tienda
        exclude = ['id_tienda']
        widgets = {
            'nombre': forms.TextInput(attrs={'maxlength':'20', 'class':'form-control cortoCentrado', 'placeholder':'Nombre de la Sucursal','onkeypress':'return validarNombre(event, this)'}),
            'direccion': forms.TextInput(attrs={'maxlength':'100','class':'form-control cortoCentrado', 'placeholder':'Dirección'}),
            'ciudad': forms.Select(attrs={'class':'form-control cortoCentrado'}),
            'comuna': forms.Select(attrs={'class':'form-control cortoCentrado'}),
            'telefono': forms.NumberInput(attrs={'class':'form-control cortoCentrado', 'onkeypress':'return validarNumero(event, this)'}),
            'correo': forms.EmailInput(attrs={'class':'form-control cortoCentrado', 'placeholder':'Correo', 'onkeypress':'return validarCorreo(event)'}),
        }

class DetalleForm(forms.ModelForm):
    class Meta:
        model = Detalle_Boleta
        exclude = ['detalle_id']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        exclude = ['id_producto']
        widgets = {
            'nombre': forms.TextInput(attrs={'maxlength':'40','class':'form-control cortoCentrado', 'placeholder':'Nombre del Producto','onkeypress':'return validarNombre(event, this)'}),
            'descripcion': forms.TextInput(attrs={'maxlength':'255','class':'form-control cortoCentrado', 'placeholder':'Descripción del Producto'}),
            'precio_base': forms.TextInput(attrs={'class':'form-control cortoCentrado', 'onkeypress':'return validarNumero(event, this)'}),
            'precio_final': forms.TextInput(attrs={'class':'form-control cortoCentrado', 'onkeypress':'return validarNumero(event, this)'}),
            'fotito': forms.ClearableFileInput(attrs={'class':'form-control cortoCentrado'}),
            'tipo': forms.Select(attrs={'class':'form-control cortoCentrado'}),
        }
    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.fields['tipo'].queryset = Tipo_Producto.objects.all()
        self.fields['tipo'].label_from_instance = lambda obj: "%s - %s" % (obj.id_tipo, obj.tipo)
        self.fields['tipo'].label = 'Tipo de Producto'

class ListaProductosOferta(forms.ModelForm):
    class Meta:
        model = Oferta
        exclude = ['producto_objetivo']

class ProductoOferta(forms.ModelForm):
    class Meta:
        model = Oferta
        exclude = ['tipo_producto_objetivo']

class FiltroProductos(forms.Form):
    tipo = forms.IntegerField(required=False)
    precio = forms.IntegerField(required=False)
    page = forms.IntegerField(required=False)