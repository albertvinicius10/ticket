from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model
from .models import Ticket, Comment
from .forms import TicketForm, CommentForm, TesteForm
from django.contrib.auth.forms import AuthenticationForm
import requests
import json

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
    if request.user.is_superuser:
        tickets = Ticket.objects.all()
    else:
        tickets = Ticket.objects.filter(staff=request.user)
    #tickets= Ticket.objects.filter(staff=request.user)
    context = {
        'tickets': tickets,
    }

    return render(request, 'helpdesk/tickets.html', context)

@login_required()
def fazendo(request):
    tickets = Ticket.objects.filter(status='Fazendo')
    tickets= Ticket.objects.all()
    if request.user.is_superuser:
        tickets = Ticket.objects.all().filter(status='Fazendo')
    else:
        tickets = Ticket.objects.filter(staff=request.user, status='Fazendo')
    context = {
        'tickets': tickets,
    }
    return render(request, 'helpdesk/fazendo.html', context)

@login_required()
def finalizado(request):
    tickets = Ticket.objects.filter(status='Feito')
    if request.user.is_superuser:
        tickets = Ticket.objects.all().filter(status='Feito')
    else:
        tickets = Ticket.objects.filter(staff=request.user, status='Feito')
    context = {
        'tickets': tickets,
    }
    return render(request, 'helpdesk/finalizado.html', context)

@login_required()
def expirado(request):
    tickets = Ticket.objects.filter(status='Expirado')
    if request.user.is_superuser:
        tickets = Ticket.objects.all().filter(status='Expirado')
    else:
        tickets = Ticket.objects.filter(staff=request.user, status='Expirado')
    context = {
        'tickets': tickets,
    }
    return render(request, 'helpdesk/finalizado.html', context)

@login_required()
def pausado(request):
    tickets = Ticket.objects.filter(status='Pausado')
    if request.user.is_superuser:
        tickets = Ticket.objects.all().filter(status='Pausado')
    else:
        tickets = Ticket.objects.filter(staff=request.user, status='Pausado')
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
    if request.method == 'POST':
        form = TesteForm(request.POST)
        if form.is_valid():
            print('hi')
            form.save()
            print(form.cleaned_data)
            usuario = request.POST.get('usuario','')
            senha = request.POST.get('senha','')
            print(usuario)
            data = {
                'usu_login': usuario,
                'usu_senha': senha,
                'usu_permissao': 'ticket',
            }
        response = requests.post('https://intra.crea-am.org.br/api/login?log',data,headers=headers,verify=False).json()
        user = authenticate(request, username=usuario, password=senha)
        print(response)
        UserModel = get_user_model()
        if response['status'] == '200':
            if not UserModel.objects.filter(username=usuario).exists():
                user=UserModel.objects.create_user(username=usuario, password=senha)
                user.save()
                login(request, user)
                return redirect('index')
            else:
                login(request, user)
                return redirect('index')
       
    
    
    else:
        form = TesteForm()

    
    #senha 1q2w3e


    
    
    return render(request, "teste.html", {'form': form})

