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
            form.save()
            return redirect('index')
    else:
        form = TicketForm()
        return render(request, 'helpdesk/add.html', {'form': form})

@login_required()
def ticket(request):
    tickets= Ticket.objects.all()
    tickets_user = User.objects.all()
    context = {
        'tickets': tickets,
        'tickets_user':tickets_user,

    }
    return render(request, 'helpdesk/tickets.html', context)