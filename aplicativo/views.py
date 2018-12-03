from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib import auth
from .models import Tipo_Usuario

def Home(request):
    return render(request, 'Mantenedores/home.html')

def Login(request):
    form = LoginForm()
    return render(request, 'Mantenedores/login.html', {'form':form})

def Auth(request):
    print('owo')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    print('owo')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        print('existe')
        auth.login(request, user)
        tipo = Tipo_Usuario.objects.get(id_tipo=2)
        print(request.user.tipo_usuario.id_tipo)
        if request.user.tipo_usuario == tipo:
            return redirect('appSupp:home')
        else:
            return redirect('appSupp:home')
    else:
        print('no existe')
        form = LoginForm()
        return render(request, 'Mantenedores/login.html', {'user': user, 'form':form})