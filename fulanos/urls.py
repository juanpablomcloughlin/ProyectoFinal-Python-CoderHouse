from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    
    path('productos/', views.lista_productos, name='ListaProductos'),
    path('productos/crear/', views.crear_producto, name='CreaProducto'),
    path('productos/editar/<int:id>/', views.editar_producto, name='EditarProducto'),
    path('productos/eliminar/<int:id>/', views.eliminarproducto, name='EliminarProducto'),
    path('detalle_producto/<int:id>/', views.detalle_producto, name='detalle_producto'),

    path('lista-pedidos/', views.PedidoList.as_view(), name='ListaPedidos'),
    path('crea-pedido/', views.PedidoCreate.as_view(), name='CreaPedido'),
    path('detalle-pedido/<int:pk>/', views.PedidoDetail.as_view(), name='DetallePedido'),
    path('actualiza-pedido/<int:pk>/', views.PedidoUpdate.as_view(), name='ActualizaPedido'),
    path('elimina-pedido/<int:pk>/', views.PedidoDelete.as_view(), name='EliminaPedido'),

    path('usuarios/', views.lista_usuarios, name='ListaUsuarios'),
    path('usuarios/crear/', views.crear_usuario, name='CreaUsuario'),
    path('editar-perfil/', views.editar_perfil, name='EditarPerfil'),
    path('agregar-avatar/', views.agregar_avatar, name='AgregarAvatar'),
    path('no_autorizado/', views.no_autorizado, name='no_autorizado'),
    path('login/', views.login_view, name='login'),
    path('registrar/', views.register, name='registrar'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='Logout'),

    path('buscar/', views.buscar_producto, name='buscar_producto'),
    path('busqueda/', views.busqueda_producto, name='busqueda_producto'),
    path('about/', views.acerca_de_mi, name='acerca_de_mi'),
    path('contacto/', views.contacto, name='contacto'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)