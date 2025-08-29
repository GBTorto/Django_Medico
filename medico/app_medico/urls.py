from django.urls import path
from . import views

urlpatterns = [
    path('add_medico/', views.add_medico)
]
