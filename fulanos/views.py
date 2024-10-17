from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Usuario, Pedido
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UsuarioFormulario, ProductoFormulario, BusquedaProductoFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

# Usuario
def crear_usuario(request):
    if request.method == 'POST':
        formulario = UsuarioFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('ListaUsuarios')  
    else:
        formulario = UsuarioFormulario()
    return render(request, 'usuario_formulario.html', {'formulario': formulario})

def lista_usuarios(request):
    usuarios = Usuario.objects.all()  
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})

def editar_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    if request.method == 'POST':
        formulario = UsuarioFormulario(request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_usuarios')
    else:
        formulario = UsuarioFormulario(instance=usuario)
    return render(request, 'usuario_formulario.html', {'formulario': formulario})

class UsuarioList(ListView):
    model = Usuario
    template_name = 'lista_usuarios.html'
    context_object_name = 'usuarios'

class UsuarioCreate(CreateView):
    model = Usuario
    template_name = 'usuario_formulario.html'
    fields = ['nombre', 'apellido', 'email']
    success_url = '/fulanos'

from django.shortcuts import redirect

def login_view(req):
    if req.method == 'POST':
        mi_formulario = AuthenticationForm(req, data=req.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            usuario = data['username']
            psw = data['password']

            user = authenticate(username=usuario, password=psw)

            if user:
                login(req, user)
                
                return render(req, "inicio.html", { "mensaje": f"Bienvenid@ {usuario}"})
            else:
                return render(req, "login.html", { "mi_formulario": mi_formulario, "mensaje": "Datos incorrectos!" })

        else:
            return render(req, "login.html", { "mi_formulario": mi_formulario })  

    else:
        mi_formulario = AuthenticationForm()
        return render(req, "login.html", { "mi_formulario": mi_formulario })

def register(req):

  if req.method == 'POST':

    mi_formulario= UserCreationForm(req.POST)
    if mi_formulario.is_valid():

      data = mi_formulario.cleaned_data
      usuario = data['username']
      mi_formulario.save()

      return render(req, "inicio.html", { "mensaje": f"Usuario {usuario} creado exitosamente!"})

    else:
      return render(req, "registro.html", { "mi_formulario": mi_formulario })    

  else:

    mi_formulario = UserCreationForm()
    return render(req, "registro.html", { "mi_formulario": mi_formulario })   

def logout_view(request):
    logout(request)
    return render(request, "logout.html")

# Producto
def crear_producto(request):
    if request.method == 'POST':
        formulario = ProductoFormulario(request.POST, request.FILES)  
        if formulario.is_valid():
            formulario.save()
            return redirect('ListaProductos')
    else:
        formulario = ProductoFormulario()
    
    return render(request, 'producto_formulario.html', {'formulario': formulario})

@login_required
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

def editar_producto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        formulario = ProductoFormulario(request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('ListaProductos')
    else:
        formulario = ProductoFormulario(instance=producto)
    return render(request, 'producto_formulario.html', {'formulario': formulario})

def eliminarproducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('ListaProductos')  
    return render(request, 'confirmar_eliminar.html', {'producto': producto})

def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'detalle_producto.html', {'producto': producto})

class ProductoDetail(DetailView):

  model = Producto
  template_name = 'producto_detail.html'
  context_object_name = 'producto'

# Pedido
class PedidoList(ListView):
    model = Pedido
    template_name = 'pedido_list.html'
    context_object_name = 'pedidos'

class PedidoDetail(DetailView):
    model = Pedido
    template_name = 'pedido_detail.html'
    context_object_name = 'pedido'

class PedidoCreate(CreateView):
    model = Pedido
    template_name = 'pedido_create.html'
    fields = ['order_number', 'producto', 'cantidad', 'usuario', 'email']  
    success_url = '/fulanos'

class PedidoUpdate(UpdateView):
    model = Pedido
    template_name = 'pedido_update.html'
    fields = ['order_number', 'producto', 'cantidad', 'usuario', 'email']
    success_url = '/fulanos/lista-pedidos/'

class PedidoDelete(DeleteView):
    model = Pedido
    template_name = 'pedido_delete.html'
    success_url = '/fulanos'
        
# Inicio
def inicio(request):
    return render(request, 'inicio.html')

# Buscar producto
def busqueda_producto(request):
    formulario = BusquedaProductoFormulario()
    return render(request, 'busqueda_producto.html', {'formulario': formulario})

def buscar_producto(request):
    formulario = BusquedaProductoFormulario(request.GET)
    if formulario.is_valid():
        nombre_producto = formulario.cleaned_data['nombre']
        productos = Producto.objects.filter(nombre__icontains=nombre_producto)
        return render(request, 'resultado_busqueda.html', {'productos': productos, 'nombre': nombre_producto})
    return render(request, 'busqueda_producto.html', {'formulario': formulario})

#About
def acerca_de_mi(request):
    return render(request, 'acerca_de_mi.html')

#404 error
def error_404_view(request, exception):
    return render(request, '404.html', status=404)