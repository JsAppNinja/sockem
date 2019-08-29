from urllib.parse import urlparse
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from api.tests.factories import TournamentFactory, UserFactory
from api.models import Tournament, User
from api.tests.unit.tournament_tests import TournamentTests
from api.util import does_url_match_id


class TournamentListTests(APITestCase):
    url = reverse('tournament-list')

    def setup_method(self, method):
        """
        Setup method run after each test.
        Creates a user, saves its token, and creates a tournament.
        """
        self.user = UserFactory()
        self.token = Token.objects.get(user_id=self.user.user_id)
        self.tournament = TournamentFactory()

    def teardown_method(self, method):
        """
        Teardown method run after each test.
        Deletes all User and Tournament objects.
        """
        Tournament.objects.all().delete()

    def test_post_create_tournament(self):
        """
        Tests POST TournamentList view
        """

        data = {
            "name": "Biggest's Pasta Tournament",
            "start_date": "2019-07-29T21:51:23Z",
            "users": []
        }

        response = self.client.post(self.url, data, format='json', HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tournament.objects.count(), 2)

        inserted_tournament = response.data
        self.assertTrue(inserted_tournament is not None)
        self.assertEqual(inserted_tournament['name'], data['name'])
        self.assertEqual(inserted_tournament['start_date'], data['start_date'])
        self.assertEqual(inserted_tournament['creator'], "http://testserver/api/users/" + str(self.user.user_id))

    def test_get_tournament(self):
        """
        Tests GET TournamentList view
        """

        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Tournament.objects.count(), 1)
        self.assertEqual(response.data['count'], 1)

        returned_tournament = response.data['results'][0]
        self.assertTrue(does_url_match_id(urlparse(returned_tournament['url']), returned_tournament['tournament_id']))
        self.assertTrue(TournamentTests.is_valid_generated_tournament_name(returned_tournament['name']))
