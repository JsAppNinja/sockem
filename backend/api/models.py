from django.db import models

# Create your models here.
class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    match_id = models.ForeignKey('Match', models.PROTECT)
    winner_id = models.ForeignKey('User', models.SET_NULL, blank=True, null=True)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)

class Match(models.Model):
    match_id = models.AutoField(primary_key=True)
    tournament_id = models.ForeignKey('Tournament', models.PROTECT)
    judge_id = models.ForeignKey('User', models.PROTECT)
    round = models.SmallIntegerField()
    num_games = models.SmallIntegerField()

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=None)
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    avatar = models.CharField(max_length=None, null=True)
