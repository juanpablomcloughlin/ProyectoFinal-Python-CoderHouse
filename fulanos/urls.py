from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views
from .views import (
    inicio,
    lista_productos,
    crear_producto,
    editar_producto,
    eliminarproducto,
    PedidoList,
    PedidoDetail,
    PedidoCreate,
    PedidoUpdate,
    PedidoDelete,
    lista_usuarios, 
    crear_usuario,
    busqueda_producto,
    buscar_producto,
    acerca_de_mi,
    register,
    login_view,
)

handler404 = 'django.views.defaults.page_not_found'

urlpatterns = [
    path('', inicio, name='inicio'),

    path('productos/', lista_productos, name='ListaProductos'),
    path('productos/crear/', crear_producto, name='CreaProducto'),
    path('productos/editar/<int:id>/', editar_producto, name='EditarProducto'),
    path('productos/eliminar/<int:id>/', eliminarproducto, name='EliminarProducto'),  
    path('detalle_producto/<int:id>/', views.detalle_producto, name='detalle_producto'),

    path('lista-pedidos/', views.PedidoList.as_view(), name='ListaPedidos'),
    path('crea-pedido/', views.PedidoCreate.as_view(), name='CreaPedido'),
    path('detalle-pedido/<int:pk>/', views.PedidoDetail.as_view(), name='DetallePedido'),
    path('actualiza-pedido/<int:pk>/', views.PedidoUpdate.as_view(), name='ActualizaPedido'),
    path('elimina-pedido/<int:pk>/', views.PedidoDelete.as_view(), name='EliminaPedido'),

    path('usuarios/', lista_usuarios, name='ListaUsuarios'),
    path('usuarios/crear/', crear_usuario, name='CreaUsuario'),
    path('busqueda/', busqueda_producto, name='busqueda_producto'),
    path('login/', login_view, name='login'),  
    path('registrar/', register, name='Registrar'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='Logout'),

    path('buscar/', buscar_producto, name='buscar_producto'),
    path('about/', acerca_de_mi, name='acerca_de_mi'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
