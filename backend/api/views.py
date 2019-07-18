"""
Class-based API views using the Django REST Framework
"""
from rest_framework import generics
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from .models import User
from .serializers import UserSerializer


class UserList(generics.ListCreateAPIView):
    """
    List all users, or create a new user.
    """
    authentication_classes = TokenAuthentication
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve, update or delete a user.
    """
    authentication_classes = TokenAuthentication
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
