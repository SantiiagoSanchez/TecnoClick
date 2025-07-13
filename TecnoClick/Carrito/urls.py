from django.urls import path
from . import views

app_name = "Carrito"

urlpatterns = [
    path("agregar/<int:producto_id>/", views.post_producto, name="agregar"),
    path("eliminar/<int:producto_id>/", views.delete_producto, name="eliminar"),
    path("restar/<int:producto_id>/", views.restar_producto, name="restar"),
    path("limpiar/", views.limpiar_carro, name="limpiar"),
]

