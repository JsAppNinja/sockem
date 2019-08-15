"""
Unit tests for the TournamentUser model in the API app
"""

import pytest
from api.tests.factories import TournamentUserFactory
from api.models import TournamentUser


class UserTests:
    """
    Class testing TournamentUser model
    """
    @pytest.mark.django_db
    def test_tournament_user_insert(self):
        """Test that we can insert a TournamentUser"""
        tournament_user = TournamentUserFactory()

        assert TournamentUser.objects.count() == 1
        assert tournament_user.user is not None
        assert tournament_user.tournament is not None
        assert tournament_user.is_judge is True
