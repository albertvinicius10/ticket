from django.db import models
from django.contrib.auth.models import User
# Create your models here.


CATEGORY = (
    ('Alta', 'Alta'),
    ('Baixa', 'Baixa'),
    ('Moderada', 'Moderada'),
)


class Ticket(models.Model):
    staff = models.ForeignKey(User, models.CASCADE, null= True)
    titulo = models.CharField(max_length=255, null=True)
    prioridade = models.CharField(max_length=20, choices=CATEGORY, null=True)
    descricao = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'ticket'

    def __str__(self):
        return f'{self.titulo} ordered by {self.staff.username}'
