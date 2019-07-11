"""
Class-based API views using the Django REST Framework
"""
from rest_framework import generics
from rest_framework import permissions
from .models import User
from .serializers import UserSerializer


class UserList(generics.ListCreateAPIView):
    """
    List all users, or create a new user.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve, update or delete a user.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
