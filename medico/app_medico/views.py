from django.shortcuts import render, redirect
from .forms import AddForm
from .models import Medico

# Create your views here.


def tela_principal(request):
    return render(request, 'app_medico/tela_principal.html')


def add_medico(request):
    # Lógica unificada para requisições POST e GET
    if request.method == 'POST':
        # Se for POST, cria o formulário com os dados enviados
        form = AddForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('/')  # Redireciona para evitar reenvio
        # Se a validação falhar, o código continua e o formulário
        # será renderizado com os dados e erros.
    else:
        # Se for GET, cria um formulário vazio
        form = AddForm() 

    # Renderiza o template, passando o formulário para ele
    return render(request, 'app_medico/add_medico.html', {'form': form})