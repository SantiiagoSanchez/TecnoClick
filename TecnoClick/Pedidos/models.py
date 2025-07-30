from django.db import models
from django.contrib.auth import get_user_model
from Tienda.models import Producto
from django.db.models import F, Sum, FloatField
# Create your models here.

User = get_user_model() #Esto nos devuelve el usuario logueado

class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
    
    @property
    def total(self):
        return self.lineapedido_set.aggregate(

            total=Sum(F("precio")*F("cantidad"), output_field=FloatField())
        )["total"]

    class Meta:
        db_table='Pedidos'
        verbose_name='Pedido'
        verbose_name_plural='Pedidos'
        ordering = ["id"]

class LineaPedido(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto_id= models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido_id= models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad= models.IntegerField(default=1)
    creado= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto_id.Nombre}'
    
    class Meta:
        db_table='LineaPedidos'
        verbose_name='Linea Pedido'
        verbose_name_plural='Linea Pedidos'
        ordering = ["id"]
