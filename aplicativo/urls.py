from django.urls import path
from aplicativo import views
from django.conf.urls import url

urlpatterns = [
    path('', views.Home, name='home'),
    path(r'sesion/login/', views.Login, name='login'),
    path(r'sesion/login/auth/', views.Auth, name='auth'),
    url('confirmado', views.ConfirmarRegistro, name='confirmado'),
    path(r'sesion/registrar/', views.Registrar, name='registrar'),
    url(r'^producto/(?P<idProducto>\w+)$', views.VerProducto, name="redir"),
    url('error', views.error, name="error"),
    url('exito', views.exito, name="exito"),
    path(r'perfil/', views.PerfilVendedor, name="perfilVendedor"),
    path(r'perfil/historial/', views.VentasVendedor, name="historial"),
    path(r'sesion/logout/', views.Logout, name="logout"),
    path(r'ofertas/', views.Ofertas, name="ofertas"),
    path(r'venta/', views.VenderProductos, name="vender"),
    url(r'^venta/boletaTerminar/(?P<idBoleta>\w+)$', views.confirmarTerminar, name="terminarBoleta"),
    url(r'^venta/boletaEliminar/(?P<idBoleta>\w+)$', views.confirmarEliminar, name="eliminarBoleta"),
    url(r'^venta/productoEliminar/(?P<idDetalle>\w+)$', views.EliminarProd, name="eliminarProd"),
    url(r'^productoAñadir/(?P<idDetalle>\w+)$', views.Añadir, name="añadir"),
    url(r'^productoSustraer/(?P<idDetalle>\w+)$', views.Sustraer, name="sustraer"),
    url(r'perfil/historial/boletaDetalle/(?P<idBoleta>\w+)$', views.Detalle, name="detalle"),
    path(r'encargado/crearTienda/', views.CrearTienda, name="crearTienda"),
    path(r'encargado/crearProducto/', views.CrearProducto, name="crearProducto"),
    path(r'encargado/asignarTienda/', views.AsigTienda, name="AsignarTienda"),
    url(r'encargado/crearOferta/(?P<tipo>\w+)$', views.CrearOferta, name="crearOferta"),
    path(r'encargado/', views.MenuEncargado, name="encargado"),
    url(r'encargado/ofertas/eliminar/(?P<idoferta>\w+)$', views.EliminarOferta, name="elimOferta"),
]
