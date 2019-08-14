"""
Unit tests for the MatchUser model in the API app
"""

import pytest
from api.tests.factories import MatchUserFactory
from api.models import MatchUser


class UserTests:
    """
    Class testing MatchUser model
    """
    @pytest.mark.django_db
    def test_match_user_insert(self):
        """Test that we can insert a MatchUser"""
        match_user = MatchUserFactory()

        assert MatchUser.objects.count() == 1
        assert match_user.user is not None
        assert match_user.match is not None
