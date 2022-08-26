from pyexpat import model
from django.db import models

# Create your models here.
class Service(models.Model):
     title = models.CharField(max_length=200, verbose_name='Título')
     subtitle = models.CharField(max_length=200)
     content = models.TextField(verbose_name="Description")
     image = models.ImageField(upload_to="services", verbose_name="Imagen")
     created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
     updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")
     