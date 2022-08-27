from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
     name = models.CharField(max_length=100, verbose_name="Nombre de la Categoría")
     created = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
     updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")
     
     class Meta:
          verbose_name = "categoría"
          verbose_name_plural = "categorías"
          ordering = ["-created"]
          
     def __str__(self):
          return self.name
     

class Post(models.Model):
     
     title = models.CharField(max_length=200, verbose_name="Título")
     content = models.TextField(verbose_name="Contenido")
     published = models.DateTimeField( default = timezone.now ,verbose_name="Fecha de publicación")
     image = models.ImageField(upload_to="blog", null=True, blank=True, verbose_name="Imagen")
     autho = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
     categories = models.ManyToManyField(Category, verbose_name="Categorías")
     created = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
     updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")
     
     class Meta:
          verbose_name = "post"
          verbose_name_plural = "posts"
          ordering = ["-created"]
     
     def __str__(self):
          return self.title