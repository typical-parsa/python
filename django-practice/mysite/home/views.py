from django.shortcuts import render
from django.http import HttpResponse
from .models import Message
# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def usershow(request, username):
    return render(request,'user/user.html', context={"name" : username})

def message_show(request):
    messages = Message.objects.all()
    return render(request, 'messages/messages.html', context={"messages" : messages})
