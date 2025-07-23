from django.urls import path
from .views import VRegistro, cerrarsesion

urlpatterns = [
    path('', VRegistro.as_view(), name="Autenticacion"),
        path('cerrar_sesion', cerrarsesion, name="cerrarsesion"),

]

