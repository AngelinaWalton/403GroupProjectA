from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Avg
from .models import *

# Create your views here.
###################
# INDEX FUNCTIONS #

def indexPageView(request) :
    return render(request, 'byulax/index.html')

# END INDEX FUNCTIONS #
#######################

###################
# ROSTER FUNCTIONS#

def rosterPageView(request):
    data = Player.objects.all().order_by("id")
    context = {
        "player": data
    }
    return render(request, 'byulax/roster.html', context)    

def addPlayer(request) :
    if request.method == 'POST' :
        new_player = Player()
        new_player.player_number = request.POST['player_number']
        new_player.first_name = request.POST['first_name']
        new_player.last_name = request.POST['last_name']
        new_player.position = request.POST['position']
        new_player.year = request.POST['year']
        new_player.save()
        return redirect('roster')
    data = Player.objects.all()
    context = {
        "players": data
    }
    return render(request, 'byulax/addRoster.html', context)

def deletePlayer(request):
    if request.method == "POST":
        try:
            stat = Player.objects.get(id = request.POST['id']).delete()
            return redirect('roster')
        except:
            return HttpResponse("Sorry, this player cannot be deleted because there are stats associated with them.")

    return  HttpResponse("Something didn't work right, please try again.")

def editPlayer(request) :
    if request.method == "POST":
        player = Player.objects.get(id = request.POST['id'])
        print(request.POST)

        new_player = Player.objects.get(id= request.POST['id'])
        new_player.player_number = request.POST['player_number']
        new_player.first_name = request.POST['first_name']
        new_player.last_name = request.POST['last_name']
        new_player.position = request.POST['position']
        new_player.year = request.POST['year']
        new_player.save()
        return redirect("roster")
    return HttpResponse("Error")

# END ROSTER FUNCTIONS #
########################

###################
# STATS FUNCTIONS #

def statsPageView(request):
    data = Stats.objects.all()
    context = {
        "stats": data
    }
    return render(request, 'byulax/stats.html', context)

def addStatsPage(request):
    if request.method == 'POST':
        new_stat = Stats()
        new_stat.ground_ball = request.POST['ground_ball']
        new_stat.goals = request.POST['goals']
        new_stat.assists = request.POST['assists']
        new_stat.points = request.POST['points']
        new_stat.face_offs = request.POST['face_offs']
        new_stat.player_id_id = request.POST['player_id']
        new_stat.game_id_id = request.POST['game_id']
        new_stat.save()
        return redirect('stats')
    playerList = Player.objects.all()
    gameList = Schedule.objects.all()
    context = {
        "players" : playerList,
        "games" : gameList
    }
    return render(request, 'byulax/addStats.html', context)

def deleteStats(request):
    if request.method == "POST":
        stat = Stats.objects.get(id = request.POST['id']).delete()
        return redirect('stats')
    return  HttpResponse("Something didn't work right, please try again.")

def totalStats(request):
    data = Stats.objects.values("player_id_id").annotate(totGb = sum('ground_ball'), totGoals = sum('goals'), totAssists = (sum('assists')), totPoints = sum('points'), totFaces = sum("face_offs"), totGoals_againts = sum('goals_against'), totSaves = sum('saves'), avgAPG = Avg('assists'), avgGPG = Avg('goals'), avgPPG = Avg('points'), avgGAA = Avg('goals_against'), avgSPG = Avg('saves'))
    context = {
        'totalStats': data
    }
    return render(request, 'byulax/totalStats.html', context)

def editStats(request):
    if request.method == "POST":
        stat = Stats.objects.get(id = request.POST['id'])

        return redirect('stats')

# END STATS FUNCTIONS #
#######################

######################
# SCHEDULE FUNCTIONS #

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

def editSchedule(request):
    if request.method == "POST":
        schedule = Schedule.object.get(date_time = 'date_time', opponent = 'opponent', location = 'location', result = 'result', info = 'info',)
        new_game = Schedule()
        new_game.date_time = request.GET['date_time']
        new_game.opponent = request.GET['opponent']
        new_game.location = request.GET['location']
        new_game.result = request.GET['result']
        new_game.info = request.GET['info']
        new_game.save()
    

def deleteSchedule(request):
    if request.method == "POST":
        try:
            scd = Schedule.objects.get(id = request.POST['id']).delete()
            return redirect('schedule')
        except:
            return HttpResponse("Sorry, this game cannot be deleted as there are stats associated with it.")
            
    return HttpResponse("Something went wrong, please try again.")
# END SCHEDULE FUNCTIONS #
##########################

    

