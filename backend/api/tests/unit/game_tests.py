"""
Unit tests for the Game model in the API app
"""

from datetime import datetime
import pytest
import pytz
from api.tests.factories import GameFactory
from api.tests.unit.user_tests import UserTests
from api.models import Game, Match, User


class GameTests:
    """
    Class testing Game model
    """
    @pytest.mark.django_db
    def test_game_insert(self):
        """Test that we can insert a Game"""
        game = GameFactory()

        assert Game.objects.count() == 1
        assert game.match is not None
        if game.winner is not None:
            assert UserTests.is_valid_generated_username(game.winner.username)
        assert game.start_time < datetime.now(tz=pytz.timezone('UTC'))
        assert game.end_time < datetime.now(tz=pytz.timezone('UTC'))
