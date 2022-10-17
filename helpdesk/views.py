from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketForm
# Create your views here.

def index(request):
    return render(request, 'helpdesk/index.html')

def add(request):
    ticket = Ticket.objects.all()
    if request.method=='POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TicketForm()
        return render(request, 'helpdesk/add.html', {'form': form})


def ticket(request):
    tickets= Ticket.objects.all()
    return render(request, 'helpdesk/tickets.html', {'tickets': tickets})