"""
Tests for TournamentUserList view
"""
from urllib.parse import urlparse
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from api.tests.factories import TournamentFactory, TournamentUserFactory, UserFactory
from api.models import Tournament, TournamentUser, User
from api.util import does_url_match_id


class TournamentUserListTests(APITestCase):
    url = reverse('tournamentuser-list')

    def setup_method(self, method):
        """
        Setup method run after each test.
        Creates a tournament and a user and saves its token.
        """
        self.user = UserFactory()
        self.token = Token.objects.get(user_id=self.user.user_id)

        self.tournament = TournamentFactory()
        self.tournamentUser = TournamentUserFactory()

    def teardown_method(self, method):
        """
        Teardown method run after each test.
        Deletes all objects.
        """
        TournamentUser.objects.all().delete()
        Tournament.objects.all().delete()
        User.objects.all().delete()

    def test_post_create_tournament_user(self):
        """
        Tests POST TournamentUserList view
        """

        data = {
            "tournament": "http://testserver/api/tournaments/" + str(self.tournament.tournament_id),
            "is_judge": True
        }

        response = self.client.post(self.url, data, format='json', HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TournamentUser.objects.count(), 2)

        inserted_tournament_user = response.data
        self.assertTrue(inserted_tournament_user is not None)

        self.assertTrue(
            does_url_match_id(
                urlparse(inserted_tournament_user['url']),
                inserted_tournament_user["tournament_user_id"])
        )
        self.assertTrue(
            does_url_match_id(
                urlparse(inserted_tournament_user["user"]),
                self.user.user_id
            )
        )
        self.assertEqual(inserted_tournament_user["user_id"], self.user.user_id)
        self.assertEqual(inserted_tournament_user['tournament'], data['tournament'])
        self.assertEqual(inserted_tournament_user['tournament_id'], self.tournament.tournament_id)
        self.assertEqual(inserted_tournament_user['is_judge'], data['is_judge'])


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
