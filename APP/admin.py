from APP.models import Productos
from APP.models import Categorias
from APP.models import Carrito
from django.contrib import admin

class ProductosAdmin (admin.ModelAdmin):
    list_display = ("id","titulo", "imagen", "descripcion", "precio" , "categoria")

class CategoriasAdmin (admin.ModelAdmin):
    list_display = ("id", "descripcion")

class CarritoAdmin (admin.ModelAdmin):
    list_display = ("id", "listaProductos", "totalCarrito")

# Register your models here.
admin.site.register(Productos, ProductosAdmin) 
admin.site.register(Categorias, CategoriasAdmin) 
admin.site.register(Carrito, CarritoAdmin)
