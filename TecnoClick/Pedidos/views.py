from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from Carrito.Carrito import Carrito
from TecnoClick.Pedidos.models import Pedido, LineaPedido
from django.contrib import messages

# Create your views here.

@login_required(login_url="/Autenticacion/loguear")
def procesar_pedido(request):
    pedido=Pedido.object.create(user=request.user)
    carrito=Carrito(request)
    lineas_pedido = list()
    for key, value in carrito.carrito.items():
        lineas_pedido.append(LineaPedido(

            producto_id=key,
            cantidad=value["Cantidad"],
            user=request.user,
            pedido=pedido

        ))

    LineaPedido.objects.bulk_create(lineas_pedido) #Esto hace muchos insert into en la tabla linea de pedidos

    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombre_user=request.username,
        email_user=request.usermail  
    )

    messages.success(request, "El pedido fue creado correctamente")

    return redirect("../store")

