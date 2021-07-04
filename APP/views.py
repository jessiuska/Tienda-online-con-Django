from APP.forms import FormAlta
from APP.models import Categorias, Productos, Carrito
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

# Create your views here.

def index(request):
    productos = Productos.objects.all().order_by('-id')[:3]
    otrosproductos = Productos.objects.all().order_by('-id')[3:10]
    categorias = Categorias.objects.all()
    titulo = Productos.objects.all()
    return render(request, "index.html", {
        'titulo': titulo,
        'productos': productos,
        'otrosproductos':otrosproductos,
        'categorias':categorias,
    })
    

def acercade(request):
    return render(request, "acercade.html")

def contacto(request):
    return render(request, "contacto.html")

class BusquedaForm(forms.Form):
    busqueda = forms.CharField(label="busqueda")
        
def busqueda(request, categ=''):
    if request.method == "POST":
        productos = Productos.objects.filter(titulo__icontains=request.POST['busqueda'])
        return render(request, 'busqueda.html', {
            'productos': productos,
            'form': BusquedaForm(),
        })
    else:
        productos = Productos.objects.filter(categoria=categ)
        return render(request, 'busqueda.html', {
            'productos': productos,
            'form': BusquedaForm(),
        })

def productosDetalles(request, pk):
    productos = get_object_or_404(Productos, id=pk)
    productos = Productos.objects.get(id=pk)
    return render(request, "producto.html" , {
        'productos':productos,
    })

@login_required(login_url='login')
def alta(request):
    if request.method == "POST":
        form = FormAlta(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormAlta() 
    else:
            categorias = Categorias.objects.all()
            form = FormAlta()
            return render(request, "alta.html" , {
                'categorias':categorias,
                'form': form,
                
            })
    return render(request, "alta.html", {
        'mensaje': 'mensaje',
        'form': form,
        })
            
def modificar(request, pk):
    productos = get_object_or_404(Productos, id=pk)
    categorias = Categorias.objects.all()
    if request.method == "POST":
        form = FormAlta(request.POST, request.FILES, instance = productos)
        if form.is_valid():
            form.save()
            
        else:
            return render(request, "modificar.html", {
                'categorias':categorias,
                'form': form,
            })
    form = FormAlta(instance = productos)
    return render(request, "modificar.html", {
        'form': form,
        'productos':productos,
       
           
    })

def eliminar(request, pk):
    productos = get_object_or_404(Productos, id=pk)
    productos.delete()
    return render(request,"index.html", {
        'productos' : Productos.objects.all().order_by('-id')[:3],
        'otrosproductos' : Productos.objects.all().order_by('-id')[3:10],
    })





