from django.db import models

# Create your models here.
class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    ]
    year = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )
    position = models.CharField(max_length = 3) #same as above
    player_number = models.PositiveSmallIntegerField()

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)
    def __str__(self):
        return (self.full_name)

class Schedule(models.Model):
    date_time = models.DateTimeField()
    location = models.CharField(max_length = 40)
    opponent = models.CharField(max_length = 40)
    result = models.CharField(max_length=7, default="0-0")
    info = models.CharField(max_length = 120, blank=True)

    def __str__(self):
        return (self.opponent + " on " + str(self.date_time)) #Im not sure this date conversion to string will work well


class Stats(models.Model):
    ground_ball = models.SmallIntegerField()
    goals = models.SmallIntegerField()
    assists = models.SmallIntegerField()
    points = models.SmallIntegerField()
    face_offs = models.SmallIntegerField()
    player_id = models.ForeignKey(Player, on_delete=models.PROTECT)
    game_id = models.ForeignKey(Schedule, on_delete= models.PROTECT)

    def __str__(self):
        return (str(self.player_id) + " and game " + str(self.game_id))

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['player_id', 'game_id'], name="game_player_CPK")
        ]