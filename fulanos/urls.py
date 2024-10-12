from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    inicio,
    lista_productos,
    crear_producto,
    editar_producto,
    eliminarproducto,
    detalle_producto, 
    lista_pedidos,
    crear_pedido,
    editar_pedido,
    lista_usuarios, 
    crear_usuario,
    busqueda_producto,
    buscar_producto,
    acerca_de_mi,
)

handler404 = 'fulanos.views.error_404_view'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('productos/', lista_productos, name='ListaProductos'),
    path('productos/crear/', crear_producto, name='CreaProducto'),
    path('productos/editar/<int:id>/', editar_producto, name='EditarProducto'),
    path('productos/eliminar/<int:id>/', eliminarproducto, name='EliminarProducto'),  # Nueva URL para eliminar
    path('productos/<int:id>/', detalle_producto, name='detalle_producto'),
    path('pedidos/', lista_pedidos, name='ListaPedidos'),
    path('pedidos/crear/', crear_pedido, name='CreaPedido'),
    path('pedidos/editar/<int:id>/', editar_pedido, name='EditarPedido'),
    path('usuarios/', lista_usuarios, name='ListaUsuarios'),
    path('usuarios/crear/', crear_usuario, name='CreaUsuario'),
    path('busqueda/', busqueda_producto, name='busqueda_producto'),
    path('buscar/', buscar_producto, name='buscar_producto'),
    path('about/', acerca_de_mi, name='acerca_de_mi'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)