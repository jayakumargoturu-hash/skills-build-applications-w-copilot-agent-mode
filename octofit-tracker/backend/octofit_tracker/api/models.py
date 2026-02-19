from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.ManyToManyField(User, related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    type = models.CharField(max_length=50)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    distance = models.FloatField(help_text='Distance in kilometers', null=True, blank=True)
    calories = models.PositiveIntegerField(null=True, blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.ManyToManyField(User, related_name='suggested_workouts', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Leaderboard(models.Model):
    team = models.OneToOneField(Team, on_delete=models.CASCADE)
    total_points = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
