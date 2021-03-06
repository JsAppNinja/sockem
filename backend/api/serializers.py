"""
Django REST Framework serializers

From the DRF docs:

Allows complex data to be converted to native Python datatypes that can then be easily rendered into
JSON, XML or other content types.

Also provide deserialization, allowing parsed data to be converted back into complex types,
after first validating the incoming data.
"""
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import User, Tournament, TournamentUser, Match, MatchUser, Game
from .util import validate_parent, validate_email


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
    users = TournamentUserSerializer(
        source='tournamentuser_set',
        read_only=False,
        many=True,
        required=False
    )
    creator = serializers.HyperlinkedRelatedField(read_only=True, view_name='user-detail')

    class Meta:
        model = Tournament
        fields = ('url', 'tournament_id', 'name', 'start_date', 'creator', 'creator_id', 'users',)
        extra_kwargs = {
            'user_id': {
                'read_only': False,
                'required': True
            }
        }
        depth = 1

    def create(self, validated_data):
        """
        Create and return a new `Tournament` instance, given the validated data.
        """
        validated_data['creator'] = self.context['request'].user
        tournament = Tournament.objects.create(**validated_data)
        return tournament

    def update(self, instance, validated_data):
        if 'name' in validated_data:
            instance.name = validated_data['name']
        if 'start_date' in validated_data:
            instance.start_date = validated_data['start_date']
        instance.save()

        return instance


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
        )

    def validate(self, attrs):
        attrs = super().validate(attrs)  # calling default validation
        parent = (attrs['parent'])
        current_round = (attrs['round'])
        if parent:
            validate_parent(parent, current_round)

        return attrs


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


class AuthCustomTokenSerializer(serializers.Serializer):
    """
    Customer serializer for tokens used to take either email or username
    """
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    email_or_username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        email_or_username = attrs.get('email_or_username')
        password = attrs.get('password')

        if email_or_username and password:
            # Check if user sent email
            if validate_email(email_or_username):
                user_request = get_object_or_404(
                    User,
                    email=email_or_username,
                )

                email_or_username = user_request.username

            user = authenticate(username=email_or_username, password=password)

            if user:
                if not user.is_active:
                    raise ValidationError('User account is disabled.')
            else:
                raise ValidationError('Unable to log in with provided credentials.')
        else:
            raise ValidationError('Must include "email or username" and "password"')

        attrs['user'] = user
        return attrs
