from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request) :
    return HttpResponse('Index')

def rosterPageView(request):
    return HttpResponse('Roster')
    
def statsPageView(request):
    return HttpResponse('Stats')


def schedulePageView(request) :
    return HttpResponse('Schedule')