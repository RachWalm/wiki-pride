from django.shortcuts import render
from .models import Event 


def index(request):
    return render(request, 'index.html')

def community(request):
    return render(request, 'community.html')

def gettoknow(request):
    return render(request, 'gettoknow.html')

def us(request):
    return render(request, 'us.html')

def sign(request):
    return render(request, 'sign.html')

def events(request):
    events_list = Event.objects.all()
    return render(request, 'events.html', {'events': events_list})