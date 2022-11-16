from django.urls import path
from .views import *

urlpatterns = [
    path('', indexPageView, name = 'index'),
    path('roster/', rosterPageView, name = 'roster'),
    path('schedule/', schedulePageView, name = 'schedule'),
    path('stats/', statsPageView, name = 'stats'),
    path('schedule/add', addSchedulePage, name= 'addSchedule'),
    path('roster/add',addPlayer, name="addRoster"),
    path('stats/add', addStatsPage, name = "addStats"),
]