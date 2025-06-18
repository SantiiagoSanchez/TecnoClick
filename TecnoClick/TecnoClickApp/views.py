from django.shortcuts import render, HttpResponse

# Create your views here.

def home (request):

    return render(request, "TecnoClickApp/home.html")

def servicios (request):

    return render(request, "TecnoClickApp/service.html")

def tienda (request):

    return render(request, "TecnoClickApp/store.html")

def blog (request):

    return render(request, "TecnoClickApp/about.html")

def contacto (request):

    return render(request, "TecnoClickApp/contact.html")
