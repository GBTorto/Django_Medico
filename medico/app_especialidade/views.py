from django.shortcuts import render, redirect
from .forms import AddForm
from .models import Especialidade

# Create your views here.
def tela_principal_especialidade(request):
    return render(request, 'app_especialidade/tela_principal_especialidade.html')

def lista_especialidades(request):
    lista = Especialidade.objects.all()

    return render(request, 'app_especialidade/especialidades_cadastradas.html', {'especialidades': lista})

def add_especialidade(request):
    if request.method == 'POST':
        form = AddForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('app_especialidade:tela_principal_especialidade')
    
    else:
        form = AddForm()

    return render(request, 'app_especialidade/add_especialidade.html', {'form': form})

# de Gabriel Morais