from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Usuario, Producto, Pedido, Avatar

class UsuarioFormulario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

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

class UserEditForm(UserChangeForm):

  password = forms.CharField(
    help_text="",
    widget=forms.HiddenInput(), required=False
  )

  password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
  password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

  class Meta:
    model = User
    fields = ('email', 'first_name', 'last_name')

  def clean_password2(self):

    print(self.cleaned_data)

    password1 = self.cleaned_data["password1"]
    password2 = self.cleaned_data["password2"]

    if password2 != password1:
      raise forms.ValidationError("Las contraseñas no son iguales")

    else:
      return password2

class AvatarFormulario(forms.ModelForm):
   class Meta:
      model=Avatar
      fields=('imagen',)

class ContactForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Tu email'}))
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tu mensaje', 'rows': 5}))