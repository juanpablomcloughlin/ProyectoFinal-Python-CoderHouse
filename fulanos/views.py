from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Usuario, Pedido, Avatar
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProductoFormulario, BusquedaProductoFormulario, ContactForm, UserEditForm, AvatarFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.contrib import messages


# Usuario
def crear_usuario(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            user = formulario.save()
            messages.success(request, f'Usuario {user.username} creado exitosamente.')
            return redirect('usuario_creado') 
    else:
        formulario = UserCreationForm()

    return render(request, 'usuario_formulario.html', {'formulario': formulario})

def usuario_creado(request):
    return render(request, 'usuario_creado.html')

def es_administrador(user):
    if not user.is_authenticated:
        return False
    return user.is_staff

def no_autorizado(request):
    return render(request, 'no_autorizado.html', {})

@login_required()
def agregar_avatar(req):

  if req.method == 'POST':

    mi_formulario= AvatarFormulario(req.POST, req.FILES)
    if mi_formulario.is_valid():

      data = mi_formulario.cleaned_data
      avatar = Avatar(user=req.user, imagen=data["imagen"])
      avatar.save() 
      return render(req, "inicio.html", { "mensaje": f"Avatar creado correctamente!"})

    else:
      return render(req, "agregar_avatar.html", { "mi_formulario": mi_formulario })    

  else:

    mi_formulario = AvatarFormulario()
    return render(req, "agregar_avatar.html", { "mi_formulario": mi_formulario })     

def lista_usuarios(request):
    usuarios = Usuario.objects.all()  
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})

@login_required
def editar_perfil(request):
    avatar_url = None
    usuario = request.user

    try:
        avatar = Avatar.objects.get(user=usuario)
        avatar_url = avatar.imagen.url if avatar.imagen else None
    except Avatar.DoesNotExist:
        avatar = None

    if request.method == 'POST':
        mi_formulario = UserEditForm(request.POST, instance=usuario) 
        if request.FILES.get('avatar'):
            if avatar:
                avatar.imagen = request.FILES['avatar']  
            else:
                avatar = Avatar(user=usuario, imagen=request.FILES['avatar']) 
            avatar.save() 

        if mi_formulario.is_valid(): 
            mi_formulario.save()  
            messages.success(request, 'Los datos han sido actualizados con éxito.')  
            return redirect('inicio') 
    else:
        mi_formulario = UserEditForm(instance=usuario)  

    return render(request, 'editar_perfil.html', {
        'mi_formulario': mi_formulario,
        'avatar_url': avatar_url,
    })
class UsuarioList(ListView):
    model = Usuario
    template_name = 'lista_usuarios.html'
    context_object_name = 'usuarios'

class UsuarioCreate(CreateView):
    model = Usuario
    template_name = 'usuario_formulario.html'
    fields = ['nombre', 'apellido', 'email']
    success_url = '/fulanos'

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
        mi_formulario = UserCreationForm(req.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            usuario = data['username']
            mi_formulario.save()

            messages.success(req, f"Usuario {usuario} creado exitosamente. ¡Ya puedes iniciar sesión!")
            return redirect('inicio')
        else:
            print(mi_formulario.errors) 
            return render(req, "registro.html", { "mi_formulario": mi_formulario })        
    else:
        mi_formulario = UserCreationForm()
        return render(req, "registro.html", { "mi_formulario": mi_formulario })

def logout_view(request):
    logout(request)
    return render(request, "logout.html")

# Producto
@login_required
def crear_producto(request):
    if not request.user.is_staff:
        return redirect('no_autorizado')  

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

@login_required
def editar_producto(request, id=None):
    if not request.user.is_staff:
        return redirect('no_autorizado')  # Redirige a la página personalizada

    producto = get_object_or_404(Producto, id=id) if id else None

    if request.method == 'POST':
        formulario = ProductoFormulario(request.POST, request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('ListaProductos')
    else:
        formulario = ProductoFormulario(instance=producto)

    return render(request, 'producto_formulario.html', {
        'formulario': formulario,
        'producto': producto,  
    })

@login_required
def eliminarproducto(request, id):
    if not request.user.is_staff:
        return redirect('no_autorizado')  # Redirige a la página personalizada

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
class PedidoList(LoginRequiredMixin, ListView):
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
    fields = ['order_number', 'producto', 'cantidad', 'email']  
    success_url = reverse_lazy('ListaPedidos') 

    def form_valid(self, form):
        form.instance.usuario = self.request.user  
        return super().form_valid(form)

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
def inicio(req):
    try:
        avatar = Avatar.objects.filter(user=req.user.id).first()  
        return render(req, "inicio.html", {'url': avatar.imagen.url})

    except:
        return render(req, "inicio.html", {})

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

#Contacto
def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Aquí no se envía el correo, solo se muestra el mensaje de éxito, a desarrollar proximamente.
            messages.success(request, "¡Tu mensaje ha sido enviado exitosamente!")
            return redirect('contacto') 

    else:
        form = ContactForm()

    return render(request, 'contacto.html', {'form': form})

#404
def handler404(request, exception):
    return render(request, '404.html', status=404)