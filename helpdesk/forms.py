from django import forms
from .models import Ticket, Comment, Teste


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['titulo','tipo', 'prioridade', 'descricao', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comentario', 'image']
    
class TesteForm(forms.ModelForm):
    class Meta:
        model = Teste
        fields = ['usuario', 'senha']

        widgets = {
            # telling Django your password field in the mode is a password input on the template
            'senha': forms.PasswordInput() 
        }