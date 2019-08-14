"""
Factories used for testing models
"""
from django.utils import timezone

from datetime import datetime
import pytz
import factory
import factory.fuzzy
from ..models import User, Tournament, Match, Game


class UserFactory(factory.django.DjangoModelFactory):
    """
    Factory for User models
    """
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'user{0}'.format(n))
    email = factory.LazyAttribute(lambda obj: '{0}@sockemboppem.com'.format(obj.username))
    password = factory.LazyAttribute(lambda obj: '{0}'.format(obj.username))


class TournamentFactory(factory.django.DjangoModelFactory):
    """
    Factory for Tournament models
    """
    class Meta:
        model = Tournament

    name = factory.Sequence(lambda n: 'tournament{0}'.format(n))
    start_date = factory.fuzzy.FuzzyDateTime(datetime.now(tz=pytz.timezone('UTC')))
    creator = factory.SubFactory(UserFactory)

    @factory.post_generation
    def users(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for user in extracted:
                self.users.add(user)


class MatchFactory(factory.django.DjangoModelFactory):
    """
    Factory for Match models
    """
    class Meta:
        model = Match

    tournament = factory.SubFactory(TournamentFactory)
    round = 1

    @factory.post_generation
    def users(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for user in extracted:
                self.users.add(user)


class GameFactory(factory.django.DjangoModelFactory):
    """
    Factory for Game models
    """

    class Meta:
        model = Game

    match = factory.SubFactory(MatchFactory)
    winner = factory.SubFactory(UserFactory)
    start_time = factory.fuzzy.FuzzyDateTime(datetime.now(tz=pytz.timezone('UTC')))
    end_time = factory.fuzzy.FuzzyDateTime(datetime.now(tz=pytz.timezone('UTC')))
