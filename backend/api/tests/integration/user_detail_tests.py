"""
Tests for UserDetail view
"""

from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from api.tests.factories import UserFactory


class UserDetailTests(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.token = Token.objects.get(user_id=self.user.user_id)

    def test_get_user_detail(self):
        """
        Tests GET UserDetail view
        """
        url = reverse('user-detail', kwargs={'pk': self.user.user_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user_id'], self.user.user_id)
        self.assertEqual(response.data['email'], self.user.email)
        self.assertEqual(response.data['username'], self.user.username)
        self.assertEqual(response.data['avatar'], self.user.avatar)
