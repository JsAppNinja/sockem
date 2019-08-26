"""
Tests for getting authentication tokens
"""
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from api.tests.factories import UserFactory
from api.util import validate_token


class GetTokenTest(APITestCase):
    url = reverse('get-token')

    def setUp(self):
        """
        Setup method run after each test.
        Creates a user and saves its token.
        """
        self.user = UserFactory()
        self.token = Token.objects.get(user_id=self.user.user_id)
        self.user.is_active = True
        self.user.username = 'username'
        self.user.set_password('password')
        self.user.save()

    def test_get_token_with_email_and_username(self):
        """
        Tests that an authentication token can be obtained by sending the user's email
        """

        data = {
            "email_or_username": self.user.email,
            "password": 'password'
        }

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data['token'])
        validate_token(response.data['token'])

        token_obtained_with_email = response.data['token']

        data['email_or_username'] = self.user.username

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data['token'])
        validate_token(response.data['token'])

        token_obtained_with_username = response.data['token']

        self.assertEqual(token_obtained_with_email, token_obtained_with_username)
        self.assertEqual(token_obtained_with_email, str(Token.objects.get(user_id=self.user.user_id)))
