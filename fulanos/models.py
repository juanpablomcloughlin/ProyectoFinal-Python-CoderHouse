from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

from django.db import models
from .models import Producto  # Asegúrate de importar el modelo Producto

class Pedido(models.Model):
    order_number = models.CharField(max_length=20)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  
    cantidad = models.IntegerField()  
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  
    email = models.EmailField()

    def __str__(self):
        return f"Pedido {self.order_number} - {self.usuario}"
