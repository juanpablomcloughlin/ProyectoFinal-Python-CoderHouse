from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Usuario, Pedido
from .forms import UsuarioFormulario, ProductoFormulario, PedidoFormulario, BusquedaProductoFormulario
from django.views.generic import ListView, CreateView

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

def lista_productos(request):
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

def eliminarproducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('ListaProductos')  
    return render(request, 'confirmar_eliminar.html', {'producto': producto})

def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'detalle_producto.html', {'producto': producto})

# Pedido
def crear_pedido(request):
    if request.method == 'POST':
        formulario = PedidoFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('ListaPedidos')  
    else:
        formulario = PedidoFormulario()
    return render(request, 'pedido_formulario.html', {'formulario': formulario})

def lista_pedidos(request):
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