from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def indexPageView(request) :
    return render(request, 'byulax/index.html')

def rosterPageView(request):
    data = Player.objects.all()
    context = {
        "player": data
    }
    return render(request, 'byulax/roster.html', context)    

def statsPageView(request):
    return render(request, 'byulax/stats.html')

def schedulePageView(request) :
    data = Schedule.objects.all()
    context = {
        "game" : data
    }
    return render(request, 'byulax/schedule.html', context)