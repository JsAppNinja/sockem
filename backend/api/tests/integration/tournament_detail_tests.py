"""
Tests for TournamentDetail view
"""

from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from api.tests.factories import UserFactory, TournamentFactory
from api.models import Tournament


class TournamentDetailTests(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.token = Token.objects.get(user_id=self.user.user_id)
        self.tournament = TournamentFactory()
        self.url = reverse('tournament-detail', kwargs={'pk': self.tournament.tournament_id})

    def test_get_tournament_detail(self):
        """
        Tests GET TournamentDetail view
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['tournament_id'], self.tournament.tournament_id)
        self.assertEqual(response.data['name'], self.tournament.name)
        self.assertEqual(response.data['start_date'], self.tournament.start_date.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
        self.assertIsNotNone(response.data['creator'])
        self.assertEqual(len(response.data['users']), 0)

    def test_put_tournament_detail(self):
        """
        Tests PUT TournamentDetail view
        """
        old_name = self.tournament.name
        old_start_date = self.tournament.start_date

        put_name = "Testing Pasta Tournament"
        put_start_date = "2006-06-06T21:51:23Z"

        data = {
            "name": put_name,
            "start_date": put_start_date,
        }

        response = self.client.put(self.url, data, format='json', HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['tournament_id'], self.tournament.tournament_id)
        self.assertEqual(response.data['name'], put_name)
        self.assertEqual(response.data['start_date'], put_start_date)
        self.assertEqual(len(response.data['users']), 0)

        self.assertNotEqual(response.data['name'], old_name)
        self.assertNotEqual(response.data['start_date'], old_start_date)

    def test_delete_tournament_detail(self):
        """
        Tests DELETE TournamentDetail view
        """
        response = self.client.delete(self.url, HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        self.assertEqual(Tournament.objects.count(), 1)
        tournament = Tournament.objects.get(tournament_id=self.tournament.tournament_id)
        self.assertIsNotNone(tournament)
