"""
Unit tests for the Match model in the API app
"""

import pytest
from api.tests.factories import MatchFactory, UserFactory
from api.tests.unit.user_tests import UserTests
from api.models import Match, MatchUser


class MatchTests:
    """
    Class testing Match model
    """
    @pytest.mark.django_db
    def test_match_insert(self):
        """Test that we can insert a Match"""
        match = MatchFactory(
            users=[UserFactory()]
        )

        assert Match.objects.count() == 1
        assert 1 <= match.round <= 100
        assert match.parent is None
        assert MatchUser.objects.count() == 1

        for user in match.users.all():
            if not UserTests.is_valid_generated_username(user.username):
                assert False
