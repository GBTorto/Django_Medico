from django.db import models
from app_especialidade.models import Especialidade

# Create your models here.
class Medico(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    crm = models.CharField(max_length=10)
    especialidade_id = models.ManyToManyField(Especialidade, related_name="especialidade")

    def __str__(self):
        return self.nome