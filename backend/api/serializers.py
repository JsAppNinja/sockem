from rest_framework import serializers
from api.models import User, Tournament, TournamentUser, TournamentJudge, Match, MatchUser, Game


class UserSerializer(serializers.ModelSerializer):
    """

    user_id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(max_length=None)
    username = serializers.CharField(max_length=16)
    password = serializers.CharField(max_length=16)
    avatar = serializers.CharField(allow_blank=True)

    """

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
