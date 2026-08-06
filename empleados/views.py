from django.shortcuts import redirect, render

from .forms import EmpleadoForm
from .models import Empleado


def home(request):
    empleados = Empleado.objects.all().order_by('-id')

    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleados:home')
    else:
        form = EmpleadoForm()

    return render(request, 'empleados/home.html', {
        'title': 'Empleados',
        'headline': 'Gestión de empleados',
        'description': 'Registra empleados y mantén su información básica organizada.',
        'form': form,
        'empleados': empleados,
    })
