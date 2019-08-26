"""
Tests for UserDetail view
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

    def test_put_user_detail(self):
        """
        Tests PUT UserDetail view
        """
        url = reverse('user-detail', kwargs={'pk': self.user.user_id})

        old_email = self.user.email
        old_username = self.user.username
        old_password = self.user.password
        old_avatar = self.user.avatar

        put_email = "testing-put@sockemboppem.com"
        put_username = "user-put-test"
        put_password = "putpassword"
        put_avatar = "http://sockemboppem.com/put-valid-url"

        data = {
            "email": put_email,
            "username": put_username,
            "password": put_password,
            "avatar": put_avatar
        }

        response = self.client.put(url, data, format='json', HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['user_id'], self.user.user_id)
        self.assertEqual(response.data['email'], put_email)
        self.assertEqual(response.data['username'], put_username)
        self.assertEqual(response.data['avatar'], put_avatar)

        self.assertNotEqual(response.data['email'], old_email)
        self.assertNotEqual(response.data['username'], old_username)
        self.assertNotEqual(response.data['avatar'], old_avatar)

        user = User.objects.get(user_id=self.user.user_id)
        self.assertNotEqual(user.password, old_password)
        self.assertEqual(user.password, put_password)

    def test_delete_user_detail(self):
        """
        Tests DELETE UserDetail view
        """
        url = reverse('user-detail', kwargs={'pk': self.user.user_id})

        response = self.client.delete(url, HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        self.assertEqual(User.objects.count(), 1)
        user = User.objects.get(user_id=self.user.user_id)
        self.assertIsNotNone(user)

