"""
Unit tests for the API app
"""

import pytest
from api.tests.factories import UserFactory


class UserTests:
    """
    Class testing User model
    """
    @pytest.mark.django_db
    def test_user_insert(self):
        """Test that we can insert a user"""
        user = UserFactory()

        print(user)

        assert user.user_id == 1
        assert user.username is not None
        assert user.email == user.username + '@sockemboppem.com'
