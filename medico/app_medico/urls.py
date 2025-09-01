from django.urls import path
from . import views

app_name = 'app_medico'

urlpatterns = [
    path('add_medico/', views.add_medico, name='add_medico')
]
