"""
Unit tests for the Tournament model in the API app
"""

from datetime import datetime
import pytest
from api.tests.factories import UserFactory, TournamentFactory
from api.tests.unit.user_tests import UserTests


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

        assert tournament.tournament_id == 1
        assert tournament.name is not None
        assert tournament.start_date is not None
        assert tournament.creator is not None
        assert tournament.users is not None

        for user in tournament.users.all():
            if not UserTests.is_valid_generated_username(user.username):
                assert False
