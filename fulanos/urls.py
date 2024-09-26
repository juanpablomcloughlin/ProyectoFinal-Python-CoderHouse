from django.urls import path
from .views import (
    inicio,
    lista_productos,
    crear_producto,
    editar_producto,
    lista_pedidos,
    crear_pedido,
    editar_pedido,
    lista_usuarios, 
    crear_usuario,
    busqueda_producto,
    buscar_producto,
)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('productos/', lista_productos, name='ListaProductos'),
    path('productos/crear/', crear_producto, name='CreaProducto'),
    path('productos/editar/<int:id>/', editar_producto, name='EditarProducto'),
    path('pedidos/', lista_pedidos, name='ListaPedidos'),
    path('pedidos/crear/', crear_pedido, name='CreaPedido'),
    path('pedidos/editar/<int:id>/', editar_pedido, name='EditarPedido'),
    path('usuarios/', lista_usuarios, name='ListaUsuarios'),
    path('usuarios/crear/', crear_usuario, name='CreaUsuario'),
    path('busqueda/', busqueda_producto, name='busqueda_producto'),
    path('buscar/', buscar_producto, name='buscar_producto'),
]