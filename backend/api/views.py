"""
Class-based API views using the Django REST Framework
"""
from rest_framework import generics
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from .models import User, Tournament
from .serializers import UserSerializer, TournamentUserSerializer, TournamentSerializer


class UserList(generics.ListCreateAPIView):
    """
    List all users, or create a new user.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve, update or delete a user.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TournamentList(generics.ListCreateAPIView):
    """
    List all tournaments, or create a new tournament
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer


class TournamentDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve, update or delete a user.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
