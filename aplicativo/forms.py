from django import forms
from django.contrib import admin
from .models import Usuario, Tienda, Oferta

class LoginForm(forms.Form):
    usuario = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'class': 'form-control cortoCentrado', 'placeholder':'Usuario', 'name':'usuario'}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control cortoCentrado', 'placeholder': 'Contraseña', 'name':'contraseña'}))

class RegistroForm(forms.ModelForm):
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control cortoCentrado', 'placeholder': 'Contraseña', 'name':'contraseña'}))
    class Meta:
        model = Usuario
        fields = ('usuario', 'email', 'tienda')
        widgets = {
            'usuario': forms.TextInput(attrs={'class':'form-control cortoCentrado', 'placeholder':'Usuario'}),
            'email': forms.EmailInput(attrs={'class':'form-control cortoCentrado', 'placeholder':'Correo Electrónico'}),
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