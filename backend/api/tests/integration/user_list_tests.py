"""
Tests for UserList view
"""
from urllib.parse import urlparse
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from api.tests.factories import UserFactory
from api.tests.unit.user_tests import UserTests
from api.models import User


class UserListTests(APITestCase):
    url = reverse('user-list')

    def setup_method(self, method):
        """
        Setup method run after each test.
        Creates a user and saves its token.
        """
        self.user = UserFactory()
        self.token = Token.objects.get(user_id=self.user.user_id)

    def teardown_method(self, method):
        """
        Teardown method run after each test.
        Deletes all User objects.
        """
        User.objects.all().delete()

    def test_post_create_user(self):
        """
        Tests POST UserList view
        """

        data = {
            "email": "user-test@sockemboppem.com",
            "username": "user-test",
            "password": "unhashedpassword",
            "avatar": "http://sockemboppem.com/some-valid-url"
        }

        response = self.client.post(self.url, data, format='json', HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

        inserted_user = response.data
        self.assertTrue(inserted_user is not None)

        self.assertEqual(inserted_user['email'], data['email'])
        self.assertEqual(inserted_user['username'], data['username'])
        self.assertRaises(KeyError, lambda: inserted_user['password'])
        self.assertEqual(inserted_user['avatar'], data['avatar'])

    def test_get_user(self):
        """
        Tests GET UserList view
        """

        response = self.client.get(self.url, format='json', HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.data['count'], 1)

        returned_user = response.data['results'][0]
        self.assertTrue(UserTests.does_url_match_user_id(urlparse(returned_user['url']), returned_user['user_id']))
        self.assertTrue(UserTests.is_valid_generated_username(returned_user['username']))
        self.assertTrue(UserTests.is_valid_generated_email(returned_user['username'], returned_user['email']))
