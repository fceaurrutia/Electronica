from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from datetime import datetime

class Tipo_Usuario(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=20)
    @classmethod
    def crear(cls, id, tipo):
        tipo_usuario = cls(id_tipo=id, tipo=tipo)
        return tipo_usuario

class UsuarioManager(UserManager):

    use_in_migrations = True

    def _create_user(self, usuario, password, **extra_fields):
        if not usuario:
            raise ValueError('Debe crear un usuario.')
        user = self.model(usuario=usuario, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, usuario, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(usuario, password, **extra_fields)

    def create_superuser(self, usuario, password, **extra_fields):
        Tipo_Usuario.crear(1, "Vendedor").save()
        Tipo_Usuario.crear(2, "Encargado").save()
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('tipo_usuario', Tipo_Usuario.objects.get(id_tipo=2))
        return self._create_user(usuario, password, **extra_fields)
        
class Tienda(models.Model):
    id_tienda = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=200)
    comuna = models.CharField(max_length=200)
    telefono = models.IntegerField()
    correo = models.EmailField()

class Usuario(AbstractBaseUser, PermissionsMixin):
    #Propiedades
    USERNAME_FIELD=('usuario')
    REQUIRED_FIELDS=['correo']
    usuario = models.CharField(('Nombre de Usuario'), max_length=12, primary_key=True)
    correo = models.EmailField(unique=True)
    is_active = models.BooleanField(('Está Activo'), default=True)
    is_staff = models.BooleanField(('Staff'), default=False)
    tipo_usuario = models.ForeignKey(Tipo_Usuario, on_delete=models.CASCADE, default=1)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE, null=True, blank=True)

    objects = UsuarioManager()

    #Metadata
    class Meta:
        ordering = ['-usuario']
 
    #Métodos
    def __str__(self):
        return self.usuario

class Tipo_Producto(models.Model):
    id_tipo = models.AutoField(('ID'), primary_key=True)
    tipo = models.CharField(('Tipo de Producto'), max_length=100)

class Producto(models.Model):
    #Propiedades
    id_producto = models.AutoField(('ID de Producto'), primary_key=True)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    tipo = models.ForeignKey(Tipo_Producto, on_delete=models.CASCADE)
    class Meta:
        ordering = ['id_producto']

class Boleta(models.Model):
    #Propiedades
    id_boleta = models.AutoField(('ID'),primary_key=True)
    fecha = models.DateField(('Fecha de Venta'), default=datetime.now)
    comentario = models.CharField(max_length=200)
    vendedor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    class Meta:
        ordering = ['id_boleta']

class Detalle_Boleta(models.Model):
    #Propiedades
    detalle_id = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    class Meta:
        ordering=['detalle_id']

class Oferta(models.Model):
    #Propiedades
    id_oferta = models.AutoField(primary_key=True)
    id_tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    tipo_producto_objetivo = models.ForeignKey(Tipo_Producto, on_delete=models.CASCADE, null=True, blank=True)
    producto_objetivo = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True)
    porcentaje = models.IntegerField(('Porcentaje de Descuento'))
    class Meta:
        ordering=['id_oferta']