from django.shortcuts import redirect, render

from .forms import GrupoForm
from .models import Grupo


def home(request):
    grupos = Grupo.objects.all().order_by('-id')

    if request.method == 'POST':
        form = GrupoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grupos:home')
    else:
        form = GrupoForm()

    return render(request, 'grupos/home.html', {
        'title': 'Grupos',
        'headline': 'Gestión de grupos',
        'description': 'Organiza tus categorías o grupos de trabajo desde una interfaz simple.',
        'form': form,
        'grupos': grupos,
    })
