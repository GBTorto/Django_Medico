from django.shortcuts import render, redirect
from .forms import AddForm
from .models import Medico
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def tela_principal(request):
    return render(request, 'app_medico/tela_principal.html')

def tela_principal_medico(request):
    return render(request, 'app_medico/tela_principal_medico.html')

# def lista_medicos(request):
#     lista = Medico.objects.all()
#     return render(request, 'app_medico/medicos_cadastrados.html', {'contacts': lista})

# def add_medico(request):
#     # Lógica unificada para requisições POST e GET
#     if request.method == 'POST':
#         # Se for POST, cria o formulário com os dados enviados
#         form = AddForm(request.POST) 
#         if form.is_valid():
#             form.save()
#             return redirect('app_medico:tela_principal_medico')  # Redireciona para evitar reenvio
#         # Se a validação falhar, o código continua e o formulário
#         # será renderizado com os dados e erros.
#     else:
#         # Se for GET, cria um formulário vazio
#         form = AddForm()

#     # Renderiza o template, passando o formulário para ele
#     return render(request, 'app_medico/add_medico.html', {'form': form})

class ListaMedico(LoginRequiredMixin, ListView):
    model = Medico
    template_name = 'app_medico/medicos_cadastrados.html'
    context_object_name = 'contacts'

class AddMedico(LoginRequiredMixin, CreateView):
    model = Medico
    form_class = AddForm
    template_name = 'app_medico/add_medico.html'
    success_url = reverse_lazy('app_medico:tela_principal_medico')

class EditarMedico(LoginRequiredMixin, UpdateView):
    model = Medico
    form_class = AddForm
    template_name = 'app_medico/add_medico.html'
    success_url = reverse_lazy('app_medico:tela_principal_medico')

class DeletarMedico(LoginRequiredMixin, DeleteView):
    model = Medico
    success_url = reverse_lazy('app_medico:medicos_cadastrados')

    def get(self, request, *args, **kwargs):
        # Força a exclusão direta, sem template
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)

# de Gabriel Morais