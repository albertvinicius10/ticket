from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.


CATEGORY = (
    ('Baixa', 'Baixa'),
    ('Moderada', 'Moderada'),
    ('Alta', 'Alta'),
    ('Crítica', 'Crítica'),
)

STATUS = (
    ('Fazendo', 'Fazendo'),
    ('Feito', 'Feito'),
    ('Expirado', 'Expirado'),
    ('Pausado', 'Pausado'),
)

OCORRENCIA = (
    ('Suporte Técnico Desktop - No Local', 'Suporte Técnico Desktop - No Local'),
    ('Suporte Técnico Desktop - Remoto', 'Suporte Técnico Desktop - Remoto'),
    ('Configuração de email', 'Configuração de email'),
    ('Suporte/Manutenção de Notebook', 'Suporte/Manutenção de Notebook'),
)

class Ticket(models.Model):
    staff = models.ForeignKey(User, models.CASCADE, null= True)
    titulo = models.CharField(max_length=255, null=True)
    prioridade = models.CharField(max_length=20, choices=CATEGORY, null=True)
    descricao = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=8, choices=STATUS,default='Fazendo')
    tipo = models.CharField(max_length=50, choices=OCORRENCIA, null=True)
    image = models.ImageField(upload_to='ocorrencia', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'ticket'

    def __str__(self):
        return f'{self.titulo} ordered by {self.staff}'
    

class Comment(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    image = models.ImageField(upload_to='comments',null=True,blank=True)

    class Meta:
        verbose_name_plural = 'comment'

class Teste(models.Model):
    usuario = models.CharField(max_length=100, null=False)
    senha = models.CharField(max_length=50, null=False)