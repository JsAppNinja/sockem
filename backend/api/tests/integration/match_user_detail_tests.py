"""
Tests for MatchUserDetail view
"""
from urllib.parse import urlparse
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from api.tests.factories import MatchFactory, MatchUserFactory, TournamentFactory, UserFactory
from api.models import Match, MatchUser, Tournament, User
from api.util import does_url_match_id


class MatchUserDetailTests(APITestCase):

    def setup_method(self, method):
        """
        Setup method runs after each test.
        Creates a User, Tournament, Match, and MatchUser
        """
        self.user = UserFactory()
        self.token = Token.objects.get(user_id=self.user.user_id)

        self.tournament = TournamentFactory()
        self.match = MatchFactory()
        self.match_user = MatchUserFactory()
        self.url = reverse('matchuser-detail', kwargs={'pk': self.match_user.match_user_id})

    def teardown_method(self, method):
        """
        Teardown method run after each test.
        Deletes all objects.
        """
        MatchUser.objects.all().delete()
        Match.objects.all().delete()
        Tournament.objects.all().delete()
        User.objects.all().delete()

    def test_get_match_user_detail(self):
        """
        Tests GET MatchUserDetail view
        """

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(
            does_url_match_id(
                urlparse(response.data['url']),
                response.data['match_user_id']
            )
        )

        self.assertTrue(response.data["user"] is not None)
        self.assertTrue(response.data['user_id'] >= 1)
        self.assertTrue(
            does_url_match_id(
                urlparse(response.data["user"]),
                response.data['user_id']
            )
        )

        self.assertTrue(response.data["match"] is not None)
        self.assertTrue(response.data['match_id'] >= 1)
        self.assertTrue(
            does_url_match_id(
                urlparse(response.data["match"]),
                response.data['match_id']
            )
        )

    def test_put_match_user_detail(self):
        """
        Tests PUT MatchUserDetail view
        """

        data = {
            "user": "http://testserver/api/users/" + str(self.user.user_id),
            "match": "http://testserver/api/matches/" + str(self.match.match_id)
        }

        response = self.client.put(self.url, data, format='json', HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(MatchUser.objects.count(), 1)
        self.assertTrue(response.data is not None)

        self.assertTrue(
            does_url_match_id(
                urlparse(response.data['url']),
                self.match_user.match_user_id
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

    def test_delete_match_user_detail(self):
        """
        Tests DELETE MatchUserDetail view
        """
        response = self.client.delete(self.url, HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(MatchUser.objects.count(), 1)
        self.assertIsNotNone(MatchUser.objects.get(match_user_id=self.match_user.match_user_id))
