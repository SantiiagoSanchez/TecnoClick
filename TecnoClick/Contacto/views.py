from django.shortcuts import render
from .forms import FormContacto
# Create your views here.

def contacto (request):

    form = FormContacto()

    return render(request, "Contacto/contact.html", {"miFormulario": form})
