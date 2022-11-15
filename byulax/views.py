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

def addStatsPage(request):
    if request.method == 'POST':
        new_game = Stats()
        new_game.ground_ball = request.POST['ground_ball']
        new_game.goals = request.POST['goals']
        new_game.assists = request.POST['assists']
        new_game.points = request.POST['points']
        new_game.face_offs = request.POST['face_offs']
        new_game.player_id = request.POST['player_id']
        new_game.game_id = request.POST['game_id']
        new_game.save()
        return redirect('stats')
    return render(request, 'byulax/addStats.html')