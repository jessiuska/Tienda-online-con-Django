
from django.shortcuts import render
from .carro import Carro
from APP.models import Productos
from django.shortcuts import redirect , get_object_or_404

# Create your views here.

def carrito(request):
    return render(request, "carrito.html")

def agregar_producto(request, producto_id):
    carro=Carro(request)
    producto=Productos.objects.get(id=producto_id)
   
    carro.agregar(producto=producto)
    return redirect("CARRO:carrito")

def eliminar_producto(request, producto_id):
    carro=Carro(request)
    producto=Productos.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect("CARRO:carrito")

def restar_producto(request, producto_id):
    carro=Carro(request)
    producto=Productos.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("CARRO:carrito")

def limpiar_carro(request):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect("CARRO:carrito")