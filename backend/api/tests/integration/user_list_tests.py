"""
Tests for UserList view
"""

from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from api.tests.factories import UserFactory
from api.models import User


class UserDetailTests(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.token = Token.objects.get(user_id=self.user.user_id)

    def test_post_create_user(self):
        """
        Tests POST UserList view
        """

        url = reverse('user-list')
        data = {
            "email": "user-test@sockemboppem.com",
            "username": "user-test",
            "password": "unhashedpassword",
            "avatar": "http://sockemboppem.com/some-valid-url"
        }

        response = self.client.post(url, data, format='json', HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

        inserted_user = User.objects.get(email='user-test@sockemboppem.com')
        self.assertTrue(inserted_user is not None)

        self.assertEqual(inserted_user.email, data['email'])
        self.assertEqual(inserted_user.username, data['username'])
        self.assertEqual(len(inserted_user.password), 78)
        self.assertEqual(inserted_user.avatar, data['avatar'])
