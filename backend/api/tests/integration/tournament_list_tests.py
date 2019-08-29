from urllib.parse import urlparse
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from api.tests.factories import TournamentFactory, UserFactory
from api.models import Tournament


class UserListTests(APITestCase):
    url = reverse('tournament-list')

    def setup_method(self, method):
        """
        Setup method run after each test.
        Creates a user and saves its token.
        """
        self.user = UserFactory()
        self.token = Token.objects.get(user_id=self.user.user_id)

        self.tournament = TournamentFactory()

    def teardown_method(self, method):
        """
        Teardown method run after each test.
        Deletes all User objects.
        """
        Tournament.objects.all().delete()

    def test_post_create_tournament(self):
        """
        Tests POST UserList view
        """

        data = {
            "name": "Biggest's Pasta Tournament",
            "start_date": "2019-07-29T21:51:23Z",
            "users": []
        }

        response = self.client.post(self.url, data, format='json', HTTP_AUTHORIZATION='Token ' + self.token.key)
        # response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tournament.objects.count(), 2)

        inserted_tournament = response.data
        self.assertTrue(inserted_tournament is not None)

        self.assertEqual(inserted_tournament['name'], data['name'])
        self.assertEqual(inserted_tournament['start_date'], data['start_date'])
        self.assertEqual(inserted_tournament['creator'], "http://testserver/api/users/" + str(self.user.user_id))

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
    #     self.assertTrue(UserTests.does_url_match_user_id(urlparse(returned_user['url']), returned_user['user_id']))
    #     self.assertTrue(UserTests.is_valid_generated_username(returned_user['username']))
    #     self.assertTrue(UserTests.is_valid_generated_email(returned_user['username'], returned_user['email']))
