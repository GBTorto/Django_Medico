from django.urls import path
from . import views

app_name = 'add_especialidade'

urlpatterns = [
    path('tela_principal_especialidade/', views.tela_principal_especialidade, name='tela_principal_especialidade'),
    path('add_especialidade/', views.add_especialidade, name="add_especialidade"),
    path('especialidades_cadastradas/', views.lista_especialidades, name='especialidades_cadastradas'),
]

# de Gabriel Morais