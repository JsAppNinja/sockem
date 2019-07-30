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
