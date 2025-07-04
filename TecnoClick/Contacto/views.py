from django.shortcuts import render, redirect
from .forms import FormContacto
# Create your views here.

def contacto (request):

    form = FormContacto()

    if request.method == "POST":
        form = FormContacto(data=request.POST)
        if form.is_valid():
            nombre = request.POST.get("Nombre")
            email = request.POST.get("Email")
            contenido = request.POST.get("Mensaje")
        
            return redirect("/contact/?valido")



    return render(request, "Contacto/contact.html", {"miFormulario": form})
