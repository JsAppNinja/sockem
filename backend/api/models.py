"""Models for REST API"""
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    """
    User model. Users can also be judges.

    Note that this class extends
    django.contrib.auth.models.AbstractUser
    and therefore inherits its fields, which
    can be further explored in the Django docs
    """
    user_id = models.AutoField(primary_key=True)
    avatar = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'user'


class Tournament(models.Model):
    """Tournament model"""
    tournament_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    creator_id = models.ForeignKey(User, models.PROTECT, related_name='tournament_creator_id')
    users = models.ManyToManyField(User, through='TournamentUser', related_name='tournament_users')
    judges = models.ManyToManyField(User, through='TournamentJudge', related_name='tournament_judges')

    class Meta:
        db_table = 'tournament'


class TournamentUser(models.Model):
    """Intermediate table for many-to-many relationship between Tournament and User"""
    tournament_user_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    tournament_id = models.ForeignKey(Tournament, on_delete=models.PROTECT)

    class Meta:
        db_table = 'tournament_user'


class TournamentJudge(models.Model):
    """Intermediate table for many-to-many relationship between Tournament and User(judge)"""
    tournament_judge_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    tournament_id = models.ForeignKey(Tournament, on_delete=models.PROTECT)

    class Meta:
        db_table = 'tournament_judge'


class Match(models.Model):
    """Match model. Round == the round in the tournament. Num_games == # games per match"""
    match_id = models.AutoField(primary_key=True)
    tournament_id = models.ForeignKey(Tournament, models.PROTECT)
    judge_id = models.ForeignKey(User, models.PROTECT, related_name='match_judge_id')
    round = models.SmallIntegerField()
    num_games = models.SmallIntegerField()
    users = models.ManyToManyField(User, through='MatchUser')

    class Meta:
        db_table = 'match'


class MatchUser(models.Model):
    """Intermediate table for many-to-many relationship between Match and User"""
    match_user_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    match_id = models.ForeignKey(Match, on_delete=models.PROTECT)

    class Meta:
        db_table = 'match_user'


class Game(models.Model):
    """Game model"""
    game_id = models.AutoField(primary_key=True)
    match_id = models.ForeignKey(Match, models.PROTECT)
    winner_id = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'game'


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    This automatically creates an authentication token whenever
    a new User is created.
    """
    if created:
        Token.objects.create(user=instance)
