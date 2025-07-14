from django.shortcuts import render, redirect
from .Carrito import Carrito
from Tienda.models import Producto
# Create your views here.

def post_producto(request, producto_id):

    carro = Carrito(request)

    producto = Producto.objects.get(id=producto_id)

    carro.addProducto(producto)

    return redirect("Tienda")

def delete_producto(request, producto_id):

    carro = Carrito(request)

    producto = Producto.objects.get(id=producto_id)

    carro.delete_producto(producto)

    return redirect("Tienda")

def restar_producto(request, producto_id):

    carro = Carrito(request)

    producto = Producto.objects.get(id=producto_id)

    carro.restarProducto(producto)

    return redirect("Tienda")

def limpiar_carro(request):

    carro = Carrito(request)

    carro.limpiarCarrito()

    return redirect("Tienda")
