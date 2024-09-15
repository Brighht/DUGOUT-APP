from django.db import models


class Laliga_Matches(models.Model):
    season = models.CharField(max_length=10)
    date = models.DateField()
    hometeam = models.CharField(max_length= 50)
    awayteam = models.CharField(max_length= 50)
    fthg = models.IntegerField() #fulltime home goals
    fthg = models.IntegerField() #fulltime home goals
    ftag = models.IntegerField() #fulltime away goals
    ftr = models.CharField(max_length=1) #fulltime results "H" or "A"
    hthg = models.FloatField() #halftime home goals
    htag = models.FloatField() #halftime away goals
    htr = models.CharField(max_length=1) #halftime results