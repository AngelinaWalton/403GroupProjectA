from django.urls import path
from .views import *

urlpatterns = [
    path('', indexPageView, name = 'index'),
    path('roster/', rosterPageView, name = 'roster'),
    path('schedule/', schedulePageView, name = 'index'),
    path('stats/', statsPageView, name = 'index'),
]