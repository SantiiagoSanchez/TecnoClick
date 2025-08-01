from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from Carrito.Carrito import Carrito
from .models import Pedido, LineaPedido
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

# Create your views here.

@login_required(login_url="/Autenticacion/loguear")
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)
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
        nombre_user=request.user.username,
        email_user=request.user.email
    )

    #Limpia el carro luego de realizar el pedido
    carrito.limpiarCarrito()

    messages.success(request, "El pedido fue creado correctamente")

    return redirect("../store")


def enviar_mail(**kwargs): #Esto es que puede recibir muchas cosas.

    asunto = "Gracias por el pedido"
    mensaje = render_to_string("emails/pedidos.html", {
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombre_user": kwargs.get("nombre_user")

    })

    mensaje_texto = strip_tags(mensaje)  #Strip tags es para que no veamos los elementos de html es decir que te devuelva solo texto legible
    from_email = "santi2005531@gmail.com"
    to="santiagosanchezz_21@hotmail.com"                     #Aca puse directamente a un correo (personal) pero tendria que ser asi:kwargs.get("email_user")

    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)  #El destinatario va entre corchetes

