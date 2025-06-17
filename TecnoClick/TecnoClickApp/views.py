from django.shortcuts import render, HttpResponse

# Create your views here.

def home (request):

    return HttpResponse("Inicio")

def servicios (request):

    return HttpResponse("Servicio")

def tienda (request):

    return HttpResponse("Tienda")

def blog (request):

    return HttpResponse("Sobre nosotros")

def contacto (request):

    return HttpResponse("Contacto")