from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('add/',views.add, name='add'),
    path('ticket/',views.ticket, name='ticket'),
    path('fazendo/', views.fazendo, name='fazendo'),
    path('finalizado/', views.finalizado, name='finalizado'),
    path('pausado/', views.pausado, name='pausado'),
    path('expirado/', views.expirado, name='expirado'),
    path('mostrar/<int:id>', views.mostrar, name='mostrar'),
    path('teste/',views.teste, name='teste'),

    
]
