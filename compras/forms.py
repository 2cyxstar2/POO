from django import forms

from .models import Compra


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['folio', 'fecha', 'subtotal', 'iva', 'total', 'proveedor']
        widgets = {
            'folio': forms.TextInput(attrs={'placeholder': 'Folio'}),
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'subtotal': forms.NumberInput(attrs={'step': '0.01', 'placeholder': '0.00'}),
            'iva': forms.NumberInput(attrs={'step': '0.01', 'placeholder': '0.00'}),
            'total': forms.NumberInput(attrs={'step': '0.01', 'placeholder': '0.00'}),
        }
