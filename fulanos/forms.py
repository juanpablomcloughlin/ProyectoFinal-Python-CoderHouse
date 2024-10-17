from django import forms
from .models import Usuario, Producto, Pedido

class UsuarioFormulario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'email']  

class ProductoFormulario(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'imagen', 'stock']  

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class PedidoFormulario(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['order_number', 'producto', 'cantidad', 'usuario', 'email']  

class BusquedaProductoFormulario(forms.Form):
    nombre = forms.CharField(label='Nombre del Producto', max_length=100)

class MiFormulario(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control text-center'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control text-center'}))