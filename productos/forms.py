from django import forms

from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'marca', 'peso', 'categoria', 'descripcion', 'color']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del producto'}),
            'marca': forms.TextInput(attrs={'placeholder': 'Marca'}),
            'peso': forms.NumberInput(attrs={'step': '0.01', 'placeholder': '0.00'}),
            'categoria': forms.TextInput(attrs={'placeholder': 'Categoría'}),
            'descripcion': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Descripción del producto'}),
            'color': forms.TextInput(attrs={'placeholder': 'Color'}),
        }
