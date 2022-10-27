from django import forms
from .models import Ticket, Comment


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['titulo','tipo', 'prioridade', 'descricao', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comentario', 'image']