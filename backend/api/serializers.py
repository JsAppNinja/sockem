"""
Django REST Framework serializers

From the DRF docs:

Allows complex data to be converted to native Python datatypes that can then be easily rendered into
JSON, XML or other content types.

Also provide deserialization, allowing parsed data to be converted back into complex types,
after first validating the incoming data.
"""

from rest_framework import serializers
from api.models import User, Tournament, TournamentUser, Match, MatchUser, Game


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'email', 'username', 'password', 'avatar')

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


class TournamentUserSerializer(serializers.HyperlinkedModelSerializer):
    """

    tournament_user_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    tournament_id = models.ForeignKey(Tournament, on_delete=models.PROTECT)
    is_judge = models.BooleanField(default=False)

    """

    user_id = serializers.ReadOnlyField(source='user.user_id')
    tournament_id = serializers.ReadOnlyField(source='tournament.tournament_id')

    class Meta:
        model = TournamentUser
        fields = ('tournament_user_id', 'user_id', 'tournament_id', 'is_judge')


# class TournamentJudgeSerializer(serializers.HyperlinkedModelSerializer):
#     """
#
#     tournament_judge_id = models.AutoField(primary_key=True)
#     user_id = models.ForeignKey(User, on_delete=models.PROTECT)
#     tournament_id = models.ForeignKey(Tournament, on_delete=models.PROTECT)
#
#     """
#
#     user_id = serializers.ReadOnlyField(source='user.user_id')
#     tournament_id = serializers.ReadOnlyField(source='tournament.tournament_id')
#
#     class Meta:
#         model = TournamentJudge
#         fields = ('tournament_judge_id', 'user_id', 'tournament_id')


class TournamentSerializer(serializers.ModelSerializer):
    """
    tournament_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    creator_id = models.ForeignKey(User, models.PROTECT, related_name='tournament_creator_id')
    users = models.ManyToManyField(User, through='TournamentUser', related_name='tournament_users')
    """

    # users = TournamentUserSerializer(source='tournament_users', read_only=True, many=True)
    users = TournamentUserSerializer(source='tournamentuser_set', read_only=True, many=True)
    # judges = TournamentJudgeSerializer(source='tournament_judges', read_only=True, many=True)

    class Meta:
        model = Tournament
        fields = ('tournament_id', 'name', 'start_date', 'creator_id', 'users')
        depth = 1

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Tournament` instance, given the validated data.
    #     """
    #     return Tournament.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Tournament` instance, given the validated data.
    #     """
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.password = validated_data.get('password', instance.password)
    #     instance.avatar = validated_data.get('avatar', instance.avatar)
    #     instance.save()
    #     return instance
