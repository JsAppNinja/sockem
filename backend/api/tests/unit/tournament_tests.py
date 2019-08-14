"""
Unit tests for the Tournament model in the API app
"""

from datetime import datetime
import pytest
import pytz
import re
from api.tests.factories import UserFactory, TournamentFactory
from api.tests.unit.user_tests import UserTests
from api.models import Tournament, TournamentUser


class TournamentTests:
    """
    Class testing Tournament model
    """
    @pytest.mark.django_db
    def test_tournament_insert(self):
        """Test that we can insert a Tournament"""
        tournament = TournamentFactory(
            users=[UserFactory()]
        )

        assert Tournament.objects.count() == 1
        assert tournament.name is not None
        assert self.is_valid_generated_tournament_name(tournament.name)
        assert tournament.start_date is not None
        assert tournament.start_date < datetime.now(tz=pytz.timezone('UTC'))
        assert tournament.creator is not None
        assert tournament.users is not None
        assert TournamentUser.objects.count() == 1

        for user in tournament.users.all():
            if not UserTests.is_valid_generated_username(user.username):
                assert False

    @staticmethod
    def is_valid_generated_tournament_name(username):
        return re.match(r'tournament\d+$', username)