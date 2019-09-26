"""
Tests for TournamentUserDetail view
"""

from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from api.tests.factories import UserFactory, TournamentFactory, TournamentUserFactory
from api.models import Tournament, TournamentUser, User


class TournamentUserDetailTests(APITestCase):

    def setup_method(self, method):
        """
        Setup method runs after each test.
        Creates a tournament, a user, a tournamentUser.
        """
        self.user = UserFactory()
        self.token = Token.objects.get(user_id=self.user.user_id)

        self.tournament = TournamentFactory()
        self.tournamentUser = TournamentUserFactory()
        self.url = reverse('tournamentuser-detail', kwargs={'pk': self.tournamentUser.tournament_user_id})

    def teardown_method(self, method):
        """
        Teardown method run after each test.
        Deletes all objects.
        """
        TournamentUser.objects.all().delete()
        Tournament.objects.all().delete()
        User.objects.all().delete()

    def test_get_tournament_user_detail(self):
        """
        Tests GET TournamentUserDetail view
        """

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['tournament_user_id'], self.tournamentUser.tournament_user_id)
        self.assertIsNotNone(response.data['user_id'])
        self.assertIsNotNone(response.data['tournament_id'])
        self.assertTrue(response.data['is_judge'])

    def test_put_tournament_user_detail_update_is_judge(self):
        """
        Tests PUT TournamentUserDetail view for updating is_judge field
        """

        data = {
            "tournament": "http://testserver/api/tournaments/" + str(self.tournament.tournament_id),
            "is_judge": False
        }

        response = self.client.put(self.url, data, format='json', HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['tournament_user_id'], self.tournamentUser.tournament_user_id)
        self.assertIsNotNone(response.data['user_id'])
        self.assertIsNotNone(response.data['tournament_id'])
        self.assertFalse(response.data['is_judge'])

    def test_put_tournament_user_detail_update_tournament(self):
        """
        Tests PUT TournamentUserDetail view for updating tournament field
        """

        new_tournament = TournamentFactory()

        data = {
            "tournament": "http://testserver/api/tournaments/" + str(new_tournament.tournament_id),
            "is_judge": True
        }

        response = self.client.put(self.url, data, format='json', HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['tournament_user_id'], self.tournamentUser.tournament_user_id)
        self.assertIsNotNone(response.data['user_id'])
        self.assertEqual(response.data['tournament_id'], new_tournament.tournament_id)
        self.assertNotEqual(response.data['tournament_id'], self.tournament.tournament_id)
        self.assertTrue(response.data['is_judge'])

    # def test_delete_Tournament_detail(self):
    #     """
    #     Tests DELETE TournamentDetail view
    #     """
    #     response = self.client.delete(self.url, HTTP_AUTHORIZATION='Token ' + self.token.key)
    #
    #     self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    #
    #     self.assertEqual(Tournament.objects.count(), 1)
    #     tournament = Tournament.objects.get(tournament_id=self.tournament.tournament_id)
    #     self.assertIsNotNone(tournament)
