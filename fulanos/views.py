from django.shortcuts import render, redirect
from .models import Producto, Usuario, Pedido
from .forms import UsuarioFormulario, ProductoFormulario, PedidoFormulario
from django.views.generic import ListView, CreateView

# Usuario
def crear_usuario(request):
    if request.method == 'POST':
        formulario = UsuarioFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_usuarios')  
    else:
        formulario = UsuarioFormulario()
    return render(request, 'usuario_formulario.html', {'formulario': formulario})

def listar_usuarios(request):
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

# Producto
def crear_producto(request):
    if request.method == 'POST':
        formulario = ProductoFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_productos')  
    else:
        formulario = ProductoFormulario()
    return render(request, 'producto_formulario.html', {'formulario': formulario})

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

def editar_producto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        formulario = ProductoFormulario(request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_productos')
    else:
        formulario = ProductoFormulario(instance=producto)
    return render(request, 'producto_formulario.html', {'formulario': formulario})

# Pedido
def crear_pedido(request):
    if request.method == 'POST':
        formulario = PedidoFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_pedidos')  
    else:
        formulario = PedidoFormulario()
    return render(request, 'pedido_formulario.html', {'formulario': formulario})

def listar_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'lista_pedidos.html', {'pedidos': pedidos})

def editar_pedido(request, id):
    pedido = Pedido.objects.get(id=id)
    if request.method == 'POST':
        formulario = PedidoFormulario(request.POST, instance=pedido)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_pedidos')
    else:
        formulario = PedidoFormulario(instance=pedido)
    return render(request, 'pedido_formulario.html', {'formulario': formulario})

# Inicio
def inicio(request):
    return render(request, 'inicio.html')

class UsuarioList(ListView):
    model = Usuario
    template_name = 'usuario_list.html'
    context_object_name = 'usuarios'

class UsuarioCreate(CreateView):
    model = Usuario
    template_name = 'usuario_create.html'
    fields = ['nombre', 'apellido', 'email']
    success_url = '/fulanos'
