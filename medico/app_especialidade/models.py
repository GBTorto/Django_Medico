from django.db import models

# Create your models here.
class Especialidade(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome