"""
Tests for MatchList view
"""
from urllib.parse import urlparse
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from api.tests.factories import UserFactory, TournamentFactory, MatchFactory
from api.tests.unit.user_tests import UserTests
from api.models import User, Tournament, Match
from api.util import does_url_match_id


class MatchListTests(APITestCase):
    url = reverse('match-list')

    def setup_method(self, method):
        """
        Setup method run after each test.
        Creates a user, tournament, match and saves the user token.
        """
        self.user = UserFactory()
        self.token = Token.objects.get(user_id=self.user.user_id)
        self.tournament = TournamentFactory()
        self.match = MatchFactory()

    def teardown_method(self, method):
        """
        Teardown method run after each test.
        Deletes all User, Tournament and Match objects.
        """
        Match.objects.all().delete()
        Tournament.objects.all().delete()
        User.objects.all().delete()

    def test_post_create_match_with_link_to_parent(self):
        """
        Tests POST MatchList view with link to a parent match
        """

        parent_match = MatchFactory()

        data = {
            "tournament": "http://testserver/api/tournaments/" + str(self.tournament.tournament_id),
            "round": 1,
            "parent": "http://testserver/api/matches/" + str(parent_match.match_id)
        }

        response = self.client.post(self.url, data, format='json', HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Match.objects.count(), 3)

        inserted_match = response.data
        self.assertTrue(inserted_match is not None)

        self.assertEqual(inserted_match['tournament'], data['tournament'])
        self.assertEqual(inserted_match['tournament_id'], self.tournament.tournament_id)
        self.assertEqual(inserted_match['round'], data['round'])
        self.assertTrue(not inserted_match['users'])
        self.assertEqual(inserted_match['parent'], data['parent'])

    def test_post_create_match_without_link_to_parent(self):
        """
        Tests POST MatchList view without link to a parent match
        """

        data = {
            "tournament": "http://testserver/api/tournaments/" + str(self.tournament.tournament_id),
            "round": 1,
            "parent": ''
        }

        response = self.client.post(self.url, data, format='json', HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Match.objects.count(), 2)

        inserted_match = response.data
        self.assertTrue(inserted_match is not None)

        self.assertEqual(inserted_match['tournament'], data['tournament'])
        self.assertEqual(inserted_match['tournament_id'], self.tournament.tournament_id)
        self.assertEqual(inserted_match['round'], data['round'])
        self.assertTrue(not inserted_match['users'])
        self.assertIsNone(inserted_match['parent'])

    # def test_get_user(self):
    #     """
    #     Tests GET UserList view
    #     """
    #
    #     response = self.client.get(self.url, format='json', HTTP_AUTHORIZATION='Token ' + self.token.key)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(User.objects.count(), 1)
    #     self.assertEqual(response.data['count'], 1)
    #
    #     returned_user = response.data['results'][0]
    #     self.assertTrue(does_url_match_id(urlparse(returned_user['url']), returned_user['user_id']))
    #     self.assertTrue(UserTests.is_valid_generated_username(returned_user['username']))
    #     self.assertTrue(UserTests.is_valid_generated_email(returned_user['username'], returned_user['email']))
