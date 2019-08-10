"""
Authentication tests for API
"""

import json, re
from django.core.urlresolvers import reverse
from rest_framework.authtoken import views as auth_views


class AuthenticationTests:
    """
    Tests token-based authentication
    """
    def test_get_super_user_token(self, rf):
        """
        Tests getting authentication tokens
        :param rf:
        :return:
        """
        request = rf.post(reverse('get-token'), {
            "username": "admin",
            "password": "password"
        })
        response = auth_views.obtain_auth_token.as_view()(request)

        assert response.status_code == 200

        content = json.loads(response.content)
        assert re.match('^[a-z0-9]*$', content['token'])
