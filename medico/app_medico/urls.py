from django.urls import path
from . import views
from .views import AddMedico, ListaMedico, EditarMedico, DeletarMedico

app_name = 'app_medico'

urlpatterns = [
    path('add_medico/', AddMedico.as_view(), name='add_medico'),
    path('tela_principal_medico/', views.tela_principal_medico, name='tela_principal_medico'),
    path('medicos_cadastrados/', ListaMedico.as_view(), name='medicos_cadastrados'),
    path('<int:pk>/editar/', EditarMedico.as_view(), name='editar_medico'),
    path('<int:pk>/deletar/', DeletarMedico.as_view(), name='deletar_medico')
]

# de Gabriel Morais