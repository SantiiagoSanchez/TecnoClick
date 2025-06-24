from django.db import models

# Create your models here.

class Servicio(models.Model):
    Titulo=models.CharField(max_length=50)
    Contenido=models.CharField(max_length=50)
    Imagen=models.ImageField(upload_to="img_servicios")
    Created=models.DateTimeField(auto_now_add=True)
    Updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
    
    def __str__(self):
        return self.Titulo