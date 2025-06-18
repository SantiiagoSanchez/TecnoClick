from django.urls import path
from TecnoClickApp import views


urlpatterns = [
    path('', views.home),
    path('service/', views.servicios),
    path('store/', views.tienda),
    path('about/', views.blog),
    path('contact/', views.contacto),
]