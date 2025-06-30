from django.shortcuts import render
from .models import Posteo,Categoria
# Create your views here.

def blog (request):
    post = Posteo.objects.all()
    return render(request, "Blog/about.html", {"posteos": post})

def categoria (request, categoria_id):

    category = Categoria.objects.get(id = categoria_id)
    post = Posteo.objects.filter(Categorias = category)
    return render(request, "Blog/categoria.html", {'Categoria': category, 'posteos': post})