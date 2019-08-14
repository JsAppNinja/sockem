"""Models for REST API"""
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework.authtoken.models import Token
from mptt.models import MPTTModel, TreeForeignKey


class User(AbstractUser):
    """
    User model. Users can also be judges.

    Note that this class extends
    django.contrib.auth.models.AbstractUser
    and therefore inherits its fields, which
    can be further explored in the Django docs
    """
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(blank=False, unique=True)
    avatar = models.URLField(blank=True, null=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return '[%s] email: %s, username: %s' % \
               (self.user_id, self.email, self.username,)

    def __repr__(self):
        return str(self.__dict__)


class Tournament(models.Model):
    """Tournament model"""
    tournament_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    creator = \
        models.ForeignKey(User, on_delete=models.PROTECT, related_name='tournament_creator_id')
    users = models.ManyToManyField(User, through='TournamentUser', related_name='tournament_users')

    class Meta:
        db_table = 'tournament'

    def __str__(self):
        return '[{0}] name: {1}, start_date: {2}, creator: {3}, users: {4}'.format(
            self.tournament_id,
            self.name,
            self.start_date,
            self.creator.user_id,
            self.users
        )

    def __repr__(self):
        return str(self.__dict__)


class TournamentUser(models.Model):
    """Intermediate table for many-to-many relationship between Tournament and User"""
    tournament_user_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    tournament = models.ForeignKey(Tournament, on_delete=models.PROTECT)
    is_judge = models.BooleanField(default=False)

    class Meta:
        db_table = 'tournament_user'

    def __str__(self):
        return '[%s] tournament: { %s }, user: { %s }, is_judge: %s' % \
               (self.tournament_user_id, self.tournament, self.user, self.is_judge)

    def __repr__(self):
        return str(self.__dict__)


class Match(MPTTModel):
    """Match model. Round == the round in the tournament. Num_games == # games per match"""
    match_id = models.AutoField(primary_key=True)
    tournament = models.ForeignKey(Tournament, models.PROTECT)
    round = models.SmallIntegerField(
        default=1,
        validators=[MaxValueValidator(100), MinValueValidator(1)]
    )
    users = models.ManyToManyField(User, through='MatchUser')
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        db_index=True
    )

    class Meta:
        """Django class meta information"""
        db_table = 'match'

    class MPTTMeta:
        """MPTT class meta information"""
        order_insertion_by = ['round']

    def __str__(self):
        return '[%s] tournament: { %s }, round: %s' % \
               (self.match_id, self.tournament, self.round)

    def __repr__(self):
        return str(self.__dict__)


class MatchUser(models.Model):
    """Intermediate table for many-to-many relationship between Match and User"""
    match_user_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    match = models.ForeignKey(Match, on_delete=models.PROTECT)

    class Meta:
        db_table = 'match_user'

    def __str__(self):
        return '[%s] user: { %s }, match: { %s }' % \
               (self.match_user_id, self.user, self.match)

    def __repr__(self):
        return str(self.__dict__)


class Game(models.Model):
    """Game model"""
    game_id = models.AutoField(primary_key=True)
    match = models.ForeignKey(Match, models.PROTECT)
    winner = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'game'

    def __str__(self):
        return '[%s] match: { %s }, winner: { %s }' % \
               (self.game_id, self.match, self.winner)

    def __repr__(self):
        return str(self.__dict__)


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    This automatically creates an authentication token whenever
    a new User is created.
    """
    if created:
        Token.objects.create(user=instance)
