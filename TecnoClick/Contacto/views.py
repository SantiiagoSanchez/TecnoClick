from django.shortcuts import render, redirect
from .forms import FormContacto
from django.core.mail import EmailMessage
# Create your views here.

def contacto (request):

    form = FormContacto()

    if request.method == "POST":
        form = FormContacto(data=request.POST)
        if form.is_valid():
            nombre = request.POST.get("Nombre")
            mail = request.POST.get("Email")
            contenido = request.POST.get("Contenido")
        
            email = EmailMessage("Mensaje desde TecnoClick", "El usuario con nombre {} con la direccion {} escribio lo siguiente:\n {}".format(nombre, mail, contenido)
                                    ,"",["santiagosanchezz_21@hotmail.com"],reply_to=[mail]) #el mail hacia donde se manda, y si queres contestarlo usas reply_to
            
            try:
                email.send()
                return redirect("/contact/?valido")
            except:
                return redirect("/contact/?novalido")



    return render(request, "Contacto/contact.html", {"miFormulario": form})
