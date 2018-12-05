from django.shortcuts import render, redirect
from .forms import *
from django.contrib import auth
from .models import *
from django.db.models import Q, Max, Min, Sum
from django.core.paginator import Paginator, Page

def Home(request):
    if request.user.is_authenticated:
        filtro = FiltroProductos(request.GET)
        prod = Producto.objects.all()
        filtroTipo = Producto.objects.order_by('tipo__id_tipo').values('tipo__tipo', 'tipo__id_tipo').distinct()
        precioMax = Producto.objects.aggregate(Max('precio_final'))
        precioMin = Producto.objects.aggregate(Min('precio_final'))
        act = ""
        if filtro.is_valid():
            if 'tipo' in request.GET and 'precio' in request.GET and not request.GET.get('tipo') is '':
                act = int(request.GET.get('tipo'))
                prod = Producto.objects.filter(Q(tipo__id_tipo=filtro.cleaned_data.get('tipo')) & Q(precio_final__lte=filtro.cleaned_data.get('precio')))
            elif 'tipo' in request.GET and not request.GET.get('tipo') is '':
                act = int(request.GET.get('tipo'))
                prod = Producto.objects.filter(Q(tipo__id_tipo=filtro.cleaned_data.get('tipo')))
            elif 'precio' in request.GET:
                prod = Producto.objects.filter(Q(precio_final__lte=filtro.cleaned_data.get('precio')))
        else:
            prod = Producto.objects.all()
        pag = Paginator(prod, 12)
        if 'page' in request.GET:
            paginaActual = request.GET.get('page')
        else:
            paginaActual = 1
        prodPag = pag.page(paginaActual)
        return render(request, 'Mantenedores/Producto/listadoProductos.html', {'productos':prodPag, 'ftipo':filtroTipo, 'min':precioMin, 'max':precioMax, 'actual':act})
    else:
        return redirect('appSupp:login')

def Logout(request):
    auth.logout(request)
    return redirect('appSupp:home')

def Login(request):
    if not request.user.is_authenticated:
        form = LoginForm()
        return render(request, 'Mantenedores/Usuario/login.html', {'form':form})
    else:
        return redirect('appSupp:home')

def Auth(request):
    username = request.POST.get('usuario', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return redirect('appSupp:home')
    else:
        form = LoginForm()
        return render(request, 'Mantenedores/Usuario/login.html', {'user': user, 'form':form})

def Registrar(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            Usuario.crear(form).save()
            return redirect('appSupp:confirmado')
        else:
            return render(request, 'Mantenedores/Usuario/registrar.html', {'form': form})
    else:
        form = RegistroForm()
        return render(request, 'Mantenedores/Usuario/registrar.html', {'form': form})

def ConfirmarRegistro(request):
    return render(request, 'Mantenedores/Mensajes/creado.html')

def VerProducto(request, idProducto):
    if request.user.is_authenticated:
        try:
            producto = Producto.objects.get(id_producto=idProducto)
            if request.method=="POST":
                form = DetalleForm(request.POST)
                try:
                    boleta = Boleta.objects.get(vendedor=request.user, terminada=False)
                except Boleta.DoesNotExist:
                    boleta = Boleta.objects.create(comentario=".", vendedor=request.user, terminada=False, sucursal=request.user.tienda)
                    boleta.save()
                if form.is_valid():
                    if Detalle_Boleta.objects.filter(id_boleta=boleta, id_producto=form.cleaned_data['id_producto']).exists():
                        det = Detalle_Boleta.objects.get(id_boleta=boleta, id_producto=form.cleaned_data['id_producto'])
                        det.cantidad += 1
                        det.calcular()
                        det.save()
                        return redirect('appSupp:vender')
                    else:
                        form.cleaned_data['id_boleta'] = boleta
                        Detalle_Boleta.crear(form).save()
                        return redirect('appSupp:vender')
        except Producto.DoesNotExist:
            return redirect('appSupp:error')
        return render(request, 'Mantenedores/Producto/verProducto.html', {'prod':producto})
    else:
        return redirect('appSupp:error')

def error(request):
    return render(request, 'Mantenedores/Mensajes/error.html')

def exito(request):
    return render(request, 'Mantenedores/Mensajes/exito.html')

def PerfilVendedor(request):
    if request.user.is_authenticated:
        stats = Boleta.objects.filter(vendedor=request.user, terminada=True)
        dinero = Detalle_Boleta.objects.filter(id_boleta__in=stats).aggregate(monis=Sum('total'))
        stats = stats.count()
        return render(request, 'Mantenedores/Usuario/perfilVendedor.html', {'ventas':stats, 'dinero':dinero})
    else:
        return redirect('appSupp:error')
    
def VentasVendedor(request):
    if request.user.is_authenticated:
        stats = Boleta.objects.filter(vendedor=request.user, terminada=True)
        return render(request, 'Mantenedores/Usuario/historialVentas.html', {'ventas':stats})
    else:
        return redirect('appSupp:error')

def Ofertas(request):
    if request.user.is_authenticated:
        off = Oferta.objects.filter(id_tienda=request.user.tienda)
        return render(request, 'Mantenedores/Producto/ofertas.html', {'ofertas':off})
    else:
        return redirect('appSupp:error')

def VenderProductos(request):
    if request.user.is_authenticated:
        try:
            boleta = Boleta.objects.get(vendedor=request.user, terminada=False)
        except Boleta.DoesNotExist:
            return render(request, 'Mantenedores/Usuario/venderProductos.html', {'boleta':None, 'productos':None})
        if request.method=="POST":
            boleta.comentario = request.POST.get('Comentario')
            boleta.save()
        productos = Detalle_Boleta.objects.filter(id_boleta=boleta.id_boleta)
        return render(request, 'Mantenedores/Usuario/venderProductos.html', {'boleta':boleta, 'productos':productos})
    else:
        return redirect('appSupp:error')

def confirmarTerminar(request, idBoleta):
    if request.user.is_authenticated:
        if idBoleta is not None:
            boleta = Boleta.objects.get(id_boleta=idBoleta)
        if request.method=="POST":
            boleta.terminada = True
            boleta.save()
            return redirect('appSupp:home')
    else:
        return redirect('appSupp:error')
    return render(request, 'Mantenedores/Boleta/terminarBoleta.html', {'boleta':boleta})

def confirmarEliminar(request, idBoleta):
    if request.user.is_authenticated:
        if idBoleta is not None:
            boleta = Boleta.objects.get(id_boleta=idBoleta)
        if request.method=="POST":
            boleta.delete()
            return redirect('appSupp:home')
    else:
        return redirect('appSupp:error')
    return render(request, 'Mantenedores/Boleta/cancelarBoleta.html', {'boleta':boleta})

def Añadir(request, idDetalle):
    det = Detalle_Boleta.objects.get(detalle_id=idDetalle)
    det.cantidad += 1
    det.calcular()
    det.save()
    return redirect('appSupp:vender')

def Sustraer(request, idDetalle):
    det = Detalle_Boleta.objects.get(detalle_id=idDetalle)
    det.cantidad -= 1
    if det.cantidad is 0:
        return redirect('appSupp:eliminarProd', idDetalle)
    else:
        det.calcular()
        det.save()
    return redirect('appSupp:vender')

def EliminarProd(request, idDetalle):
    if request.user.is_authenticated:
        if idDetalle is not None:
            det = Detalle_Boleta.objects.get(detalle_id=idDetalle)
        if request.method=="POST":
            det.delete()
            return redirect('appSupp:vender')
    else:
        return redirect('appSupp:error')
    return render(request, 'Mantenedores/Boleta/eliminarProducto.html', {'detalle':det})

def Detalle(request, idBoleta):
    if request.user.is_authenticated:
        try:
            boleta = Boleta.objects.get(vendedor=request.user, id_boleta=idBoleta)
        except Boleta.DoesNotExist:
            return redirect('appSupp:error')
        productos = Detalle_Boleta.objects.filter(id_boleta=boleta.id_boleta)
        return render(request, 'Mantenedores/Boleta/detalleBoleta.html', {'boleta':boleta, 'productos':productos})
    else:
        return redirect('appSupp:error')

def CrearTienda(request):
    if request.user.is_authenticated and request.user.tipo_usuario.id_tipo == 2:
        if request.method=="POST":
            form = TiendaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('appSupp:exito')
        else:
            form = TiendaForm()
        return render(request, 'Mantenedores/Tienda/crearTienda.html', {'form':form})
    else:
        return redirect('appSupp:error')
        
def MenuEncargado(request):
    if request.user.is_authenticated and request.user.tipo_usuario.id_tipo == 2:
        return render(request, 'Mantenedores/Usuario/encargado.html')
    else:
        return redirect('appSupp:error')

def CrearProducto(request):
    if request.user.is_authenticated and request.user.tipo_usuario.id_tipo == 2:
        if request.method=="POST":
            form = ProductoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('appSupp:exito')
        else:
            form = ProductoForm()
        return render(request, 'Mantenedores/Producto/crearProducto.html', {'form':form})
    else:
        return redirect('appSupp:error')

def AsigTienda(request):
    if request.user.is_authenticated and request.user.tipo_usuario.id_tipo == 2:
        if request.method=="POST":
            form = AsignarTienda(request.POST)
            if form.is_valid():
                form.Guardar(request.POST.get('sujeto'), request.POST.get('tienda'))
                return redirect('appSupp:exito')
        else:
            form = AsignarTienda()
        return render(request, 'Mantenedores/Tienda/asigVendedor.html', {'form':form})
    else:
        return redirect('appSupp:error')
        