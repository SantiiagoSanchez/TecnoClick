from django.shortcuts import render, redirect
from .Carrito import Carrito
from Tienda.models import Producto
# Create your views here.

def post_producto(request, idProd):

    carro = Carrito(request)

    producto = Producto.objects.get(id=idProd)

    carro.addProducto(producto)

    return redirect("store")

def delete_producto(request, idProd):

    carro = Carrito(request)

    producto = Producto.objects.get(id=idProd)

    carro.delete_producto(producto)

    return redirect("store")

def restar_producto(request, idProd):

    carro = Carrito(request)

    producto = Producto.objects.get(id=idProd)

    carro.restarProducto(producto)

    return redirect("store")

def limpiar_carro(request):

    carro = Carrito(request)

    carro.limpiarCarrito()

    return redirect("store")
