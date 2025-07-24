from django.urls import path
from .views import VRegistro, cerrarsesion, logear

urlpatterns = [
    path('', VRegistro.as_view(), name="Autenticacion"),
    path('cerrar_sesion', cerrarsesion, name="cerrarsesion"),
    path('logear', logear, name="logear"),


]

