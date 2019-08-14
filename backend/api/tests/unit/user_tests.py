"""
Unit tests for the User model in the API app
"""

import pytest
import re
from api.tests.factories import UserFactory


class UserTests:
    """
    Class testing User model
    """
    @pytest.mark.django_db
    def test_user_insert(self):
        """Test that we can insert a user"""
        user = UserFactory()

        # assert user.user_id == 3
        assert user.username is not None
        assert self.is_valid_generated_username(user.username)
        assert user.email == user.username + '@sockemboppem.com'

    @staticmethod
    def is_valid_generated_username(username):
        return re.match(r'user\d+$', username)
