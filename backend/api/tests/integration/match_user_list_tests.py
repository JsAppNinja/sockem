"""
Tests for MatchUserList view
"""
from urllib.parse import urlparse
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from api.tests.factories import MatchFactory, MatchUserFactory, TournamentFactory, UserFactory
from api.models import Match, MatchUser, Tournament, User
from api.util import does_url_match_id


class MatchUserListTests(APITestCase):
    url = reverse('matchuser-list')

    def setup_method(self, method):
        """
        Setup method runs after each test.
        Creates a Tournament, User, Match and MatchUser.
        """
        self.user = UserFactory()
        self.token = Token.objects.get(user_id=self.user.user_id)

        self.tournament = TournamentFactory()
        self.match = MatchFactory()
        self.match_user = MatchUserFactory()

    def teardown_method(self, method):
        """
        Teardown method run after each test.
        Deletes all objects.
        """
        MatchUser.objects.all().delete()
        Match.objects.all().delete()
        Tournament.objects.all().delete()
        User.objects.all().delete()

    def test_post_create_match_user(self):
        """
        Tests POST MatchUserList view
        """

        data = {
            "user": "http://testserver/api/users/" + str(self.user.user_id),
            "match": "http://testserver/api/matches/" + str(self.match.match_id)
        }

        response = self.client.post(self.url, data, format='json', HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MatchUser.objects.count(), 2)

        self.assertTrue(response.data is not None)

        self.assertTrue(
            does_url_match_id(
                urlparse(response.data['url']),
                response.data["match_user_id"]
            )
        )

        self.assertTrue(
            does_url_match_id(
                urlparse(response.data["user"]),
                self.user.user_id
            )
        )
        self.assertEqual(response.data["user_id"], self.user.user_id)

        self.assertTrue(
            does_url_match_id(
                urlparse(response.data["match"]),
                self.match.match_id
            )
        )
        self.assertEqual(response.data["match_id"], self.match.match_id)

    def test_get_match_user(self):
        """
        Tests GET MatchUserList view
        """

        response = self.client.get(self.url, format='json', HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(MatchUser.objects.count(), 1)
        self.assertEqual(response.data['count'], 1)
        self.assertIsNone(response.data['next'])
        self.assertIsNone(response.data['previous'])

        returned_match_user = response.data['results'][0]
        self.assertTrue(
            does_url_match_id(
                urlparse(returned_match_user['url']),
                returned_match_user['match_user_id']
            )
        )

        self.assertTrue(returned_match_user["user"] is not None)
        self.assertTrue(returned_match_user['user_id'] >= 1)
        self.assertTrue(
            does_url_match_id(
                urlparse(returned_match_user["user"]),
                returned_match_user['user_id']
            )
        )

        self.assertTrue(returned_match_user["match"] is not None)
        self.assertTrue(returned_match_user['match_id'] >= 1)
        self.assertTrue(
            does_url_match_id(
                urlparse(returned_match_user["match"]),
                returned_match_user['match_id']
            )
        )
