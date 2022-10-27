from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages 
from .models import Ticket, Comment
from .forms import TicketForm, CommentForm
import requests
import json
import urllib3
# Create your views here.
@login_required()
def index(request):
    return render(request, 'helpdesk/index.html')
@login_required()
def add(request):
    ticket = Ticket.objects.all()
    if request.method=='POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.status = 'Fazendo'
            instance.staff = request.user
            instance.save()
            return redirect('index')
    else:
        form = TicketForm()
        return render(request, 'helpdesk/add.html', {'form': form})

@login_required()
def ticket(request):
    tickets= Ticket.objects.all()
    #tickets= Ticket.objects.filter(staff=request.user)
    context = {
        'tickets': tickets,
    }

    return render(request, 'helpdesk/tickets.html', context)

@login_required()
def fazendo(request):
    tickets = Ticket.objects.filter(status='Fazendo')
    context = {
        'tickets': tickets,
    }
    return render(request, 'helpdesk/fazendo.html', context)

@login_required()
def finalizado(request):
    tickets = Ticket.objects.filter(status='Feito')
    context = {
        'tickets': tickets,
    }
    return render(request, 'helpdesk/finalizado.html', context)

@login_required()
def expirado(request):
    tickets = Ticket.objects.filter(status='Expirado')
    context = {
        'tickets': tickets,
    }
    return render(request, 'helpdesk/finalizado.html', context)

@login_required()
def pausado(request):
    tickets = Ticket.objects.filter(status='Pausado')
    context = {
        'tickets': tickets,
    }
    return render(request, 'helpdesk/finalizado.html', context)

@login_required()
def mostrar(request, id):
    tickets = Ticket.objects.get(pk=id)
    comments = Comment.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('mostrar',id=id)
    else:
        form = CommentForm()
    context = {
        'tickets': tickets,
        'comments': comments,
        'form': form,
    }
    return render(request, 'helpdesk/mostrar.html', context)

def teste(request):
    
    headers = requests.utils.default_headers()

    headers.update(
        {
            'User-Agent': 'My User Agent 1.0',
            'X-CRE44M': 'APP'
        }
    )

    data = {
        'usu_login': '02323384260',
        'usu_senha': '1q2w3e',
        'usu_permissao': 'ticket',
    }

    response = requests.post('https://intra.crea-am.org.br/api/login?log',data,headers=headers,verify=False).json()
    print(response)
    return render(request, "teste.html", {'response': response})
