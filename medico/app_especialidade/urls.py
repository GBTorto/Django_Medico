from django.urls import path
from . import views
from .views import AddEspecialidade, ListaEspecialidade, EditarEspecialidade, DeletarEspecialidade

app_name = 'add_especialidade'

urlpatterns = [
    path('tela_principal_especialidade/', views.tela_principal_especialidade, name='tela_principal_especialidade'),
    path('add_especialidade/', AddEspecialidade.as_view(), name="add_especialidade"),
    path('especialidades_cadastradas/', ListaEspecialidade.as_view(), name='especialidades_cadastradas'),
    path('<int:pk>/editar/', EditarEspecialidade.as_view(), name='editar_especialidade'),
    path('<int:pk>/deletar/', DeletarEspecialidade.as_view(), name='deletar_especialidade')
]

# de Gabriel Morais