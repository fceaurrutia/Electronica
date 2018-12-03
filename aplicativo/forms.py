from django import forms
from django.contrib import admin
from .models import Usuario, Tienda, Oferta

class LoginForm(forms.Form):
    usuario = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'class': 'form-control cortoCentrado', 'placeholder':'Usuario', 'name':'usuario'}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control cortoCentrado', 'placeholder': 'Contraseña', 'name':'contraseña'}))

class RegistroForm(forms.ModelForm):
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    class Meta:
        model = Usuario
        fields = ('usuario', 'email')

class ADMUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        exclude = ['is_staff', 'is_superuser']

#Forms para la web.

class TiendaForm(forms.ModelForm):
    class Meta:
        model = Tienda
        exclude = ['id_tienda']

class ListaProductosOferta(forms.ModelForm):
    class Meta:
        model = Oferta
        exclude = ['producto_objetivo']

class ProductoOferta(forms.ModelForm):
    class Meta:
        model = Oferta
        exclude = ['tipo_producto_objetivo']