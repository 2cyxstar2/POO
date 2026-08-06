from django import forms

from .models import cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = ['nombre', 'apellido', 'sexo', 'tipo', 'direccion']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre completo'}),
            'apellido': forms.TextInput(attrs={'placeholder': 'Apellido'}),
            'sexo': forms.TextInput(attrs={'placeholder': 'Femenino o Masculino'}),
            'tipo': forms.TextInput(attrs={'placeholder': 'Regular, VIP, etc.'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Dirección completa'}),
        }
