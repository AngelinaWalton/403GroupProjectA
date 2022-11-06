from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request) :
    return render(request, 'byulax/index.html')

def rosterPageView(request):
    return render(request, 'byulax/roster.html')    

def statsPageView(request):
    return render(request, 'byulax/stats.html')

def schedulePageView(request) :
    return render(request, 'byulax/schedule.html')