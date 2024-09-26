from django.urls import path
from .views import (
    inicio,
    listar_productos, crear_producto, editar_producto,
    listar_pedidos, crear_pedido, editar_pedido,
    listar_usuarios, crear_usuario, editar_usuario
)

urlpatterns = [
    path('', inicio, name='inicio'),

    # Rutas para productos
    path('productos/', listar_productos, name='ListaProductos'),
    path('productos/crear/', crear_producto, name='CreaProducto'),
    path('productos/editar/<int:id>/', editar_producto, name='EditarProducto'),

    # Rutas para pedidos
    path('pedidos/', listar_pedidos, name='ListaPedidos'),
    path('pedidos/crear/', crear_pedido, name='CreaPedido'),
    path('pedidos/editar/<int:id>/', editar_pedido, name='EditarPedido'),

    # Rutas para usuarios
    path('usuarios/', listar_usuarios, name='ListaUsuarios'),
    path('usuarios/crear/', crear_usuario, name='CreaUsuario'),
    path('usuarios/editar/<int:id>/', editar_usuario, name='EditarUsuario'),
]