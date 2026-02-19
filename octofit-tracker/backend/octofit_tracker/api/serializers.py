from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Team, Activity, Workout, Leaderboard

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Team
        fields = ['id', 'name', 'members', 'created_at']

class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    team = TeamSerializer(read_only=True)
    class Meta:
        model = Activity
        fields = ['id', 'user', 'team', 'type', 'duration', 'distance', 'calories', 'date', 'created_at']

class WorkoutSerializer(serializers.ModelSerializer):
    suggested_for = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'suggested_for', 'created_at']

class LeaderboardSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    class Meta:
        model = Leaderboard
        fields = ['id', 'team', 'total_points', 'last_updated']
