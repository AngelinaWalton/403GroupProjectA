from django.urls import path
from .views import *

urlpatterns = [
    path('', indexPageView, name = 'index'),
    path('roster/', rosterPageView, name = 'roster'),
    path('roster/add/',addPlayer, name="addRoster"),
    path('roster/delete/', deletePlayer, name="deletePlayer"),
    path('schedule/', schedulePageView, name = 'schedule'),
    path('schedule/add/', addSchedulePage, name= 'addSchedule'),
    path('schedule/delete/', deleteSchedule, name="deleteSchedule"),
    path('stats/', statsPageView, name = 'stats'),
    path('stats/add/', addStatsPage, name = "addStats"),
    path('stats/delete/', deleteStats, name="deleteStats"),
]