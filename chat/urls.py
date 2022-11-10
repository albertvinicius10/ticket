from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
 
 
urlpatterns = [
    path("chat", views.home, name="chat-home"),
    path('home/', views.home, name='chat-home'),
    path('send/', views.send_chat, name='chat-send'),
    path('renew/', views.get_messages, name='chat-renew'),
]