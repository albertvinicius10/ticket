from django.contrib import admin
from .models import Ticket
from .models import Room
# Register your models here.

admin.site.register(Ticket)
admin.site.register(Room)