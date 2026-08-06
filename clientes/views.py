from django.shortcuts import render, redirect

from .forms import ClienteForm
from .models import cliente

# Create your views here.


def home(request):
    return form_clientes(request)


def form_clientes(request):
    clientes_db = cliente.objects.all().order_by('-id')

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes:form-clientes')
    else:
        form = ClienteForm()

    return render(request, 'clientes/form.html', {
        'title': 'Formulario de Clientes',
        'form': form,
        'clientes_db': clientes_db,
    })
