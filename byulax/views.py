from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request) :
    return render(request, 'byulax/index.html')

def rosterPageView(request):
    return HttpResponse('Roster' + "git test")
    
def statsPageView(request):
    return HttpResponse('Stats')


def schedulePageView(request) :
    return HttpResponse('Schedule')