from django import forms
from .models import Usuario, Producto, Pedido

class UsuarioFormulario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'email']  

class ProductoFormulario(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock']  

class PedidoFormulario(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['usuario', 'producto', 'cantidad']  