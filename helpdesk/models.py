from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


CATEGORY = (
    ('Alta', 'Alta'),
    ('Baixa', 'Baixa'),
    ('Moderada', 'Moderada'),
)


class Ticket(models.Model):
    titulo = models.CharField(max_length=255, null=True)
    prioridade = models.CharField(max_length=20, choices=CATEGORY, null=True)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo
    
