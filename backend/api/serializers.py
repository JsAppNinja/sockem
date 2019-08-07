"""
Django REST Framework serializers

From the DRF docs:

Allows complex data to be converted to native Python datatypes that can then be easily rendered into
JSON, XML or other content types.

Also provide deserialization, allowing parsed data to be converted back into complex types,
after first validating the incoming data.
"""

from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import User, Tournament, TournamentUser, Match, MatchUser, Game
from .util import validate_parent


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for User model
    """
    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = ('url', 'user_id', 'email', 'username', 'password', 'avatar',)

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """

        return User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            password=make_password(validated_data['password']),
            avatar=validated_data['avatar']
        )

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


class TournamentUserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for TournamentUser model
    """
    user = serializers.HyperlinkedRelatedField(read_only=True, view_name='user-detail')
    tournament = serializers.HyperlinkedRelatedField(
        queryset=Tournament.objects.all(),
        read_only=False,
        view_name='tournament-detail'
    )

    class Meta:
        model = TournamentUser
        fields = (
            'url',
            'tournament_user_id',
            'user',
            'user_id',
            'tournament',
            'tournament_id',
            'is_judge',
        )

    def create(self, validated_data):
        """
        Create and return a new `TournamentUser` instance, given the validated data.
        """
        validated_data['user'] = self.context['request'].user
        tournament_user = TournamentUser.objects.create(**validated_data)
        return tournament_user


class TournamentSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Tournament model
    """
    users = TournamentUserSerializer(source='tournamentuser_set', read_only=False, many=True,)
    creator = serializers.HyperlinkedRelatedField(read_only=True, view_name='user-detail')

    class Meta:
        model = Tournament
        fields = ('url', 'tournament_id', 'name', 'start_date', 'creator', 'creator_id', 'users',)
        depth = 1

    def create(self, validated_data):
        """
        Create and return a new `Tournament` instance, given the validated data.
        """
        user_data = validated_data.pop('tournamentuser_set')
        validated_data['creator'] = self.context['request'].user
        tournament = Tournament.objects.create(**validated_data)
        tournament_user = \
            TournamentUser.objects.create(
                user=validated_data['creator'],
                tournament=tournament,
                is_judge=user_data[0]['is_judge']
            )
        tournament_user.save()
        return tournament


class MatchUserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for MatchUser model
    """
    user = serializers.HyperlinkedRelatedField(
        queryset=User.objects.all(),
        view_name='user-detail'
    )
    match = serializers.HyperlinkedRelatedField(
        queryset=Match.objects.all(),
        view_name='match-detail'
    )

    class Meta:
        model = MatchUser
        fields = ('url', 'match_user_id', 'user', 'user_id', 'match', 'match_id',)

    def create(self, validated_data):
        """
        Create and return a new `MatchUser` instance, given the validated data.
        """
        match_user = MatchUser.objects.create(**validated_data)
        return match_user


class MatchSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Match model
    """
    tournament = serializers.HyperlinkedRelatedField(
        queryset=Tournament.objects.all(),
        view_name='tournament-detail'
    )
    users = MatchUserSerializer(source='matchuser_set', read_only=True, many=True,)
    # prev_matches = serializers.HyperlinkedRelatedField(
    #     queryset=Match.objects.all(),
    #     read_only=False,
    #     many=True,
    #     view_name='match-detail',
    # )

    class Meta:
        model = Match
        fields = (
            'url',
            'match_id',
            'tournament',
            'tournament_id',
            'round',
            'users',
            'parent',
            # 'prev_matches',
        )

    def validate(self, attrs):
        attrs = super().validate(attrs)  # calling default validation
        parent = (attrs['parent'])
        current_round = (attrs['round'])
        if parent:
            validate_parent(self, parent, current_round)

        return attrs

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Match` instance, given the validated data.
    #     """
    #     prev_matches = (*validated_data["prev_matches"],)
    #     match = Match.objects.create(
    #         tournament=validated_data['tournament'],
    #         round=validated_data['round'],
    #     )
    #     for prev_match in prev_matches:
    #         match.prev_matches.add(prev_match)
    #     return match


class GameSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Game model
    """
    match = serializers.HyperlinkedRelatedField(
        queryset=Match.objects.all(),
        view_name='match-detail'
    )
    winner = serializers.HyperlinkedRelatedField(
        queryset=User.objects.all(),
        view_name='user-detail'
    )

    class Meta:
        model = Game
        fields = (
            'url',
            'game_id',
            'match',
            'match_id',
            'winner',
            'winner_id',
            'start_time',
            'end_time'
        )

    def create(self, validated_data):
        """
        Create and return a new `Game` instance, given the validated data.
        """
        game = Game.objects.create(**validated_data)
        return game
