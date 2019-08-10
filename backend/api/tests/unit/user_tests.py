"""
Unit tests for the API app
"""

import pytest
from backend.api.tests.factories import UserFactory


class UserTests:
    """
    Class testing User model
    """
    @pytest.mark.django_db
    def test_user_insert(self):
        """Test that we can insert a user"""
        user = UserFactory()

        assert user.count() == 2
