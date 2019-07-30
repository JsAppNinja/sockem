"""
Class-based API views using the Django REST Framework
"""
from rest_framework import generics
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from .models import User, Tournament, TournamentUser, Match, MatchUser
from . import serializers


class UserList(generics.ListCreateAPIView):
    """
    List all users, or create a new user.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve, update or delete a user.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class TournamentList(generics.ListCreateAPIView):
    """
    List all tournaments, or create a new tournament
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Tournament.objects.all()
    serializer_class = serializers.TournamentSerializer


class TournamentDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve, update or delete a tournament.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Tournament.objects.all()
    serializer_class = serializers.TournamentSerializer


class TournamentUserList(generics.ListCreateAPIView):
    """
    List all tournament users, or create a new tournament user
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = TournamentUser.objects.all()
    serializer_class = serializers.TournamentUserSerializer


class TournamentUserDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve, update or delete a tournament user.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = TournamentUser.objects.all()
    serializer_class = serializers.TournamentUserSerializer


class MatchList(generics.ListCreateAPIView):
    """
    List all matches, or create a new Match
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Match.objects.all()
    serializer_class = serializers.MatchSerializer


class MatchDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve, update or delete a match.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Match.objects.all()
    serializer_class = serializers.MatchSerializer


class MatchUserList(generics.ListCreateAPIView):
    """
    List all match users, or create a new match user
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = MatchUser.objects.all()
    serializer_class = serializers.MatchUserSerializer


class MatchUserDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve, update or delete a match user.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = MatchUser.objects.all()
    serializer_class = serializers.MatchUserSerializer
