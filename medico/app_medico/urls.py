from django.urls import path
from . import views

app_name = 'app_medico'

urlpatterns = [
    path('add_medico/', views.add_medico, name='add_medico'),
    path('tela_principal_medico/', views.tela_principal_medico, name='tela_principal_medico'),
    path('medicos_cadastrados/', views.lista_medicos, name='medicos_cadastrados'),
]

# de Gabriel Morais