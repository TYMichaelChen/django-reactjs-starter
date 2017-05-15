from __future__ import unicode_literals

from django.db import models

class Workout(models.Model):

    WALK = 10 
    JOG = 20
    RUN = 30
    SPRINT = 40
    WORKOUT_CHOICES = (
        (WALK, 'Walking workout'),
        (JOG, 'Jogging workout'),
        (RUN, 'Running workout'),
        (SPRINT, 'Sprint workout'),
    )
    type = models.IntegerField(choices=WORKOUT_CHOICES, default=RUN)
    date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey('Location', blank=True, null=True, related_name="workouts")


class Location(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)

    map_lat = models.FloatField(blank=True, null=True)
    map_long = models.FloatField(blank=True, null=True)