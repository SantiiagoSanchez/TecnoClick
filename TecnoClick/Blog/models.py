from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categoria(models.Model):
    Nombre = models.CharField(max_length=30)
    Created=models.DateTimeField(auto_now_add=True)
    Updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
    
    def __str__(self):
        return self.Nombre
    
class Posteo(models.Model):
    Titulo = models.CharField(max_length=30)
    Contenido = models.CharField(max_length=70)
    Imagen = models.ImageField(upload_to='img_blog', null=True, blank=True)
    Autor = models.ForeignKey(User, on_delete=models.CASCADE) #Esto es para borrar todos los posteos cuando demos de baja un autor
    Categorias = models.ManyToManyField(Categoria) #Relacion de muchos a muchos
    Created=models.DateTimeField(auto_now_add=True)
    Updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Posteo"
        verbose_name_plural = "Posteos"
    
    def __str__(self):
        return self.Titulo