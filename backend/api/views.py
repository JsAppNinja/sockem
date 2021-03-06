"""
Class-based API views using the Django REST Framework
"""

from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


from .models import User, Tournament, TournamentUser, Match, MatchUser, Game
from . import serializers


@api_view(['GET'])
def api_root(request, format=None):
    """
    View for the API_root

    :return: All the API endpoints that the user can navigate via hyperlinks
    """
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'tournaments': reverse('tournament-list', request=request, format=format),
        'tournament_users': reverse('tournamentuser-list', request=request, format=format),
        'matches': reverse('match-list', request=request, format=format),
        'match_users': reverse('matchuser-list', request=request, format=format),
        'games': reverse('game-list', request=request, format=format),
    })


@permission_classes([])
class UserList(generics.ListCreateAPIView):
    """
    List all users, or create a new user.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.get_queryset().order_by('user_id')
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
    queryset = Tournament.objects.get_queryset().order_by('tournament_id')
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
    queryset = TournamentUser.objects.get_queryset().order_by('tournament_user_id')
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
    List all matches, or create a new Match.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Match.objects.get_queryset().order_by('match_id')
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
    List all match users, or create a new match user.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = MatchUser.objects.get_queryset().order_by('match_user_id')
    serializer_class = serializers.MatchUserSerializer


class MatchUserDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve, update or delete a match user.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = MatchUser.objects.all()
    serializer_class = serializers.MatchUserSerializer


class GameList(generics.ListCreateAPIView):
    """
    List all games, or create a new game.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Game.objects.get_queryset().order_by('game_id')
    serializer_class = serializers.GameSerializer


class GameDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve, update or delete a game.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Game.objects.all()
    serializer_class = serializers.GameSerializer


class ObtainAuthToken(APIView):
    """ Used to get a token based on either username or email """
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (
        FormParser,
        MultiPartParser,
        JSONParser,
    )

    renderer_classes = (JSONRenderer,)

    def post(self, request):
        """ Send post request for token"""
        serializer = serializers.AuthCustomTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        content = {
            'token': str(token.key),
        }

        return Response(content)
