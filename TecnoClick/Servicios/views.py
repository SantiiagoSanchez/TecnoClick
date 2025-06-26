from django.shortcuts import render
from Servicios.models import Servicio

# Create your views here.

def servicios (request):
    Service = Servicio.objects.all()
    return render(request, "Servicios/service.html", {"servicios": Service})