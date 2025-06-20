from django.urls import path
from TecnoClickApp import views


urlpatterns = [
    path('', views.home, name="Inicio"),
    path('service/', views.servicios, name="Servicio"),
    path('store/', views.tienda, name="Tienda"),
    path('about/', views.blog, name="Blog"),
    path('contact/', views.contacto, name="Contacto"),
]