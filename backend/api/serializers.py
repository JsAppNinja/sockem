"""
Django REST Framework serializers

From the DRF docs:

Allows complex data to be converted to native Python datatypes that can then be easily rendered into
JSON, XML or other content types.

Also provide deserialization, allowing parsed data to be converted back into complex types,
after first validating the incoming data.
"""

from rest_framework import serializers
from .models import User, Tournament, TournamentUser, Match, MatchUser, Game


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model
    """
    class Meta:
        model = User
        fields = ('user_id', 'email', 'username', 'password', 'avatar',)

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.save()
        return instance


class TournamentUserSerializer(serializers.ModelSerializer):
    """
    Serializer for TournamentUser model
    """
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    tournament = serializers.PrimaryKeyRelatedField(queryset=Tournament.objects.all())

    class Meta:
        model = TournamentUser
        fields = ('tournament_user_id', 'user', 'tournament', 'is_judge',)

    def create(self, validated_data):
        """
        Create and return a new `TournamentUser` instance, given the validated data.
        """
        tournament_user = TournamentUser.objects.create(**validated_data)
        return tournament_user


class TournamentSerializer(serializers.ModelSerializer):
    """
    Serializer for Tournament model
    """
    users = TournamentUserSerializer(source='tournamentuser_set', read_only=False, many=True,)
    creator = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Tournament
        fields = ('tournament_id', 'name', 'start_date', 'creator', 'users',)
        depth = 1

    def create(self, validated_data):
        """
        Create and return a new `Tournament` instance, given the validated data.
        """
        user_data = validated_data.pop('tournamentuser_set')
        tournament = Tournament.objects.create(**validated_data)
        tournament_user = \
            TournamentUser.objects.create(
                user=validated_data['creator'],
                tournament=tournament,
                is_judge=user_data[0]['is_judge']
            )
        tournament_user.save()
        return tournament


class MatchUserSerializer(serializers.ModelSerializer):
    """
    Serializer for MatchUser model
    """
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    match = serializers.PrimaryKeyRelatedField(queryset=Match.objects.all())

    class Meta:
        model = MatchUser
        fields = ('match_user_id', 'user', 'match',)

    def create(self, validated_data):
        """
        Create and return a new `MatchUser` instance, given the validated data.
        """
        match_user = MatchUser.objects.create(**validated_data)
        return match_user


class MatchSerializer(serializers.ModelSerializer):
    """
    Serializer for Match model
    """
    tournament = serializers.PrimaryKeyRelatedField(queryset=Tournament.objects.all())
    users = MatchUserSerializer(source='matchuser_set', read_only=True, many=True,)

    class Meta:
        model = Match
        fields = ('match_id', 'tournament', 'round', 'users',)

    def create(self, validated_data):
        """
        Create and return a new `Match` instance, given the validated data.
        """
        match = Match.objects.create(**validated_data)
        return match


class GameSerializer(serializers.ModelSerializer):
    """
    Serializer for Game model
    """
    match = serializers.PrimaryKeyRelatedField(queryset=Match.objects.all())
    winner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Game
        fields = ('game_id', 'match', 'winner', 'start_time', 'end_time')

    def create(self, validated_data):
        """
        Create and return a new `Game` instance, given the validated data.
        """
        game = Game.objects.create(**validated_data)
        return game
