from django import forms
from .models import Productos
from .models import Carrito

class FormAlta(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ('titulo','imagen','descripcion', 'categoria', 'precio')


