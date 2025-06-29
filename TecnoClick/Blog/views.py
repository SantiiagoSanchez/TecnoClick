from django.shortcuts import render
from .models import Posteo
# Create your views here.

def blog (request):
    post = Posteo.objects.all()
    return render(request, "Blog/about.html", {"posteos": post})