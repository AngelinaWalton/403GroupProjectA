from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Avg, Sum
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
        player = Player.objects.get(id= request.POST['id'])
        player.player_number = request.POST['player_number']
        player.first_name = request.POST['first_name']
        player.last_name = request.POST['last_name']
        player.position = request.POST['position']
        player.year = request.POST['year']
        player.save()
        return redirect("roster")
    return HttpResponse("Error")


def searchRoster(request):
    if request.method == "POST":
        try:
            search = request.POST['searchInput'].split(' ')
            fname = search[0]
            lname = search[1]
            player = Player.objects.get(first_name = fname, last_name = lname)
            print(fname + " " + lname + " " + str(player))
            context = {
                "player" : [player]
            }
            return render(request, 'byulax/roster.html', context)     
        except:
            return redirect("roster")
# END ROSTER FUNCTIONS #
########################

###################
# STATS FUNCTIONS #

def statsPageView(request):
    data = Stats.objects.select_related('player_id', 'game_id').all().order_by("player_id_id")
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
        new_stat.goals_against = request.POST['goals_against']
        new_stat.saves = request.POST['saves']
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
    data = Stats.objects.values("player_id_id", "player_id_id__first_name", "player_id_id__last_name", 'player_id_id__player_number').annotate(totGb = Sum('ground_ball'), totGoals = Sum('goals'), totAssists = Sum('assists'), totPoints = Sum('points'), totFaces = Sum("face_offs"), totGoals_against = Sum('goals_against'), totSaves = Sum('saves'), avgAPG = Avg('assists'), avgGPG = Avg('goals'), avgPPG = Avg('points'), avgGAA = Avg('goals_against'), avgSPG = Avg('saves')).order_by('player_id_id')
    context = {
        'totalStats': data
    }
    return render(request, 'byulax/totalStats.html', context)

def editStats(request):
    if request.method == "POST":
        stat = Stats.objects.get(id = request.POST['id'])
        stat.ground_ball = request.POST['ground_ball']
        stat.goals = request.POST['goals']
        stat.assists = request.POST['assists']
        stat.points = request.POST['points']
        stat.face_offs = request.POST['face_offs']
        stat.goals_against = request.POST['goals_against']
        stat.saves = request.POST['saves']
        stat.save()
        return redirect('stats')

# END STATS FUNCTIONS #
#######################

######################
# SCHEDULE FUNCTIONS #

def schedulePageView(request) :
    data = Schedule.objects.all().order_by("date_time")
    for each in data:
        print(each.date_time)
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
        byuscore = request.POST['byuscore']
        oppscore = request.POST['oppscore']
        result = str(byuscore) + '-' + str(oppscore)
        new_game.result = result
        new_game.info = request.POST['info']
        new_game.save()
        return redirect('schedule')
    return render(request, 'byulax/addSchedule.html')

def editSchedule(request):
    if request.method == "POST":
        editSchedule = Schedule.objects.get(id=request.POST["id"])
        editSchedule.date_time = request.POST['date_time']
        editSchedule.opponent = request.POST['opponent']
        editSchedule.location = request.POST['location']
        editSchedule.result = request.POST['result']
        editSchedule.info = request.POST['info']
        editSchedule.save()
        return redirect('schedule')
    return HttpResponse('Error')
    

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

    

