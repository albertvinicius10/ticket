from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages 
from .models import Ticket
from .forms import TicketForm
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
