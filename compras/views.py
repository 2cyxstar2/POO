from django.shortcuts import redirect, render

from .forms import CompraForm
from .models import Compra


def home(request):
    compras = Compra.objects.all().order_by('-id')

    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('compras:home')
    else:
        form = CompraForm()

    return render(request, 'compras/home.html', {
        'title': 'Compras',
        'headline': 'Registro de compras',
        'description': 'Gestiona compras, proveedores y montos desde un solo lugar.',
        'form': form,
        'compras': compras,
    })
