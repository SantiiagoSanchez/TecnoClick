from django.db import models

# Create your models here.

class CategoriaProd(models.Model):
    Nombre = models.CharField(max_length=50)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="CategoriaProd"
        verbose_name_plural="CategoriasProd"

    def __str__(self):
        return self.Nombre
    
class Producto(models.Model):
    Nombre = models.CharField(max_length=50)
    Categoria = models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    Imagen = models.ImageField(upload_to="img_productos", null=True, blank=True)
    Precio = models.FloatField()
    Disponibilidad = models.BooleanField(default=True)

    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"