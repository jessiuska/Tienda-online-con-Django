from io import IncrementalNewlineDecoder
from django.db import models


# Create your models here.
class Categorias(models.Model):
    id = models.IntegerField(primary_key=IncrementalNewlineDecoder)
    descripcion = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id} {self.descripcion}"

class Productos(models.Model):
    id = models.IntegerField(primary_key=IncrementalNewlineDecoder)
    titulo = models.CharField(max_length=64)
    imagen = models.ImageField(upload_to="ventas", null=False)
    descripcion = models.CharField(max_length=64)
    precio = models.FloatField()
    categoria = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.id} {self.titulo} ({self.imagen}) ({self.descripcion}) ({self.precio}) ({self.categoria})"
    
class Carrito(models.Model):
    id = models.IntegerField(primary_key=IncrementalNewlineDecoder)
    usuario = models.CharField(max_length=64)
    listaProductos = models.CharField(max_length=64)
    totalCarrito = models.FloatField()
    
    def __str__(self):
        return f"{self.id} {self.usuario} ({self.listaProductos}) ({self.totalCarrito})"        

        
