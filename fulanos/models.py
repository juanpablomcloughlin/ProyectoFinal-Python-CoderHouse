from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    fecha_creacion= models.DateField(auto_now_add=True)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Pedido(models.Model):
    order_number = models.CharField(max_length=20)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  
    cantidad = models.IntegerField()  
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  
    email = models.EmailField()

    def __str__(self):
        return f"Pedido {self.order_number} - {self.producto.nombre}"

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True, null=True)

    def __str__(self):
        return f"Avatar de {self.user.username}"