from django.shortcuts import render, redirect
from .forms import AddForm
from .models import Especialidade
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def tela_principal_especialidade(request):
    return render(request, 'app_especialidade/tela_principal_especialidade.html')

# def lista_especialidades(request):
#     lista = Especialidade.objects.all()

#     return render(request, 'app_especialidade/especialidades_cadastradas.html', {'especialidades': lista})

# def add_especialidade(request):
#     if request.method == 'POST':
#         form = AddForm(request.POST)

#         if form.is_valid():
#             form.save()

#             return redirect('app_especialidade:tela_principal_especialidade')
    
#     else:
#         form = AddForm()

#     return render(request, 'app_especialidade/add_especialidade.html', {'form': form})

class ListaEspecialidade(LoginRequiredMixin, ListView):
    model = Especialidade
    template_name = 'app_especialidade/especialidades_cadastradas.html'
    context_object_name = 'especialidades'

class AddEspecialidade(LoginRequiredMixin, CreateView):
    model = Especialidade
    form_class = AddForm
    template_name = 'app_especialidade/add_especialidade.html'
    success_url = reverse_lazy('app_especialidade:tela_principal_especialidade')

class EditarEspecialidade(LoginRequiredMixin, UpdateView):
    model = Especialidade
    form_class = AddForm
    template_name = 'app_especialidade/add_especialidade.html'
    success_url = reverse_lazy('app_especialidade:tela_principal_especialidade')

class DeletarEspecialidade(LoginRequiredMixin, DeleteView):
    model = Especialidade
    success_url = reverse_lazy('app_especialidade:especialidades_cadastradas')

    def get(self, request, *args, **kwargs):
        # Força a exclusão direta, sem template
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)

# de Gabriel Morais