"""
Unit tests for the Tournament model in the API app
"""

from datetime import datetime
import pytest
from api.tests.factories import UserFactory, TournamentFactory


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

        print("IN TOURNAMENT_TESTS")
        print(tournament)
        print(tournament.name)
        print(tournament.start_date)
        print(tournament.creator)
        print(tournament.users)

        """
        tournament_id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=32, blank=True, null=True)
        start_date = models.DateTimeField(blank=True, null=True)
        creator = \
            models.ForeignKey(User, on_delete=models.PROTECT, related_name='tournament_creator_id')
        users = models.ManyToManyField(User, through='TournamentUser', related_name='tournament_users')
        """

        assert tournament.tournament_id == 1
        assert tournament.name is not None
        assert tournament.start_date is not None
        assert tournament.creator is not None
        assert tournament.users is not None
