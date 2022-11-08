from django.db import models

# Create your models here.
class Player(models.model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField()
    year = models.ForeignKey() #what goes in the parenthesis?
    position = models.ForeignKey() #same as above
    player_number = models.PositiveSmallIntegerField(max_length=3)

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)
    def __str__(self):
        return (self.full_name)

class Schedule(models.model):
    date_time = models.DateTimeField()
    location = models.CharField(max_length = 40)
    opponent = models.CharField(max_length = 40)
    result = models.CharField(max_length=7, default="0-0")
    info = models.CharField(max_length = 120, blank=True)

    def __str__(self):
        return (self.Opponent + " on " + str(self.date_time)) #Im not sure this date conversion to string will work well


