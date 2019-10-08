"""
Tests for MatchDetail view
"""

from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from api.tests.factories import MatchFactory, UserFactory, TournamentFactory, TournamentUserFactory
from api.models import Match, Tournament, TournamentUser, User


class MatchDetailTests(APITestCase):

    def setup_method(self, method):
        """
        Setup method runs after each test.
        Creates a tournament, a user, a tournamentUser.
        """
        self.user = UserFactory()
        self.token = Token.objects.get(user_id=self.user.user_id)

        self.tournament = TournamentFactory()
        self.match = MatchFactory()
        self.url = reverse('match-detail', kwargs={'pk': self.match.match_id})

    def teardown_method(self, method):
        """
        Teardown method run after each test.
        Deletes all User, Tournament and Match objects.
        """
        Match.objects.all().delete()
        Tournament.objects.all().delete()
        User.objects.all().delete()

    def test_get_match_detail(self):
        """
        Tests GET MatchDetail view
        """

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['url'], "http://testserver/api/matches/" + str(self.match.match_id))
        self.assertEqual(response.data['match_id'], self.match.match_id)
        self.assertEqual(
            response.data['tournament'],
            "http://testserver/api/tournaments/" + str(self.match.tournament_id)
        )
        self.assertEqual(response.data['tournament_id'], self.match.tournament_id)
        self.assertEqual(response.data['round'], self.match.round)
        self.assertIsNone(response.data['parent'])

    def test_put_match_detail(self):
        """
        Tests PUT MatchDetail view
        """
        new_tournament = TournamentFactory()
        parent_match = MatchFactory()

        data = {
            "tournament": "http://testserver/api/tournaments/" + str(new_tournament.tournament_id),
            "round": 1,
            "parent": "http://testserver/api/matches/" + str(parent_match.match_id)
        }

        response = self.client.put(self.url, data, format='json', HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data is not None)
        self.assertEqual(response.data['tournament'], data['tournament'])
        self.assertEqual(response.data['tournament_id'], new_tournament.tournament_id)
        self.assertEqual(response.data['round'], data['round'])
        self.assertEqual(response.data['parent'], data['parent'])

    def test_delete_match_detail(self):
        """
        Tests DELETE MatchDetail view
        """
        response = self.client.delete(self.url, HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(Match.objects.count(), 1)
        self.assertIsNotNone(Match.objects.get(match_id=self.match.match_id))
