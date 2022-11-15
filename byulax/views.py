from django.shortcuts import render, redirect
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

def addSchedulePage(request):
    if request.method == 'POST':
        new_game = Schedule()
        new_game.date_time = request.POST['date']
        new_game.location = request.POST['location']
        new_game.opponent = request.POST['opponent']
        new_game.result = request.POST['result']
        new_game.info = request.POST['info']
        new_game.save()
        return redirect('schedule')
    return render(request, 'byulax/addSchedule.html')

def addPlayer(request) :
    if request.method == 'POST' :
        new_player = Player()
        new_player.player_number = request.POST['player_number']
        new_player.first_name = request.POST['first_name']
        new_player.last_name = request.POST['last_name']
        new_player.position = request.POST['position']
        new_player.year = request.POST['year']
        return redirect('roster')
    return render(request, 'byulax/addRoster.html')