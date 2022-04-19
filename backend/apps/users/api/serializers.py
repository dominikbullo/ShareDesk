from rest_framework import serializers

from django.conf import settings

from apps.teams.api.serializers import TeamSerializer
from apps.users.models import User
from core.choices import UserTypeChoices


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField(read_only=True)
    status = serializers.SerializerMethodField(read_only=True)
    full_name = serializers.SerializerMethodField(read_only=True)
    short_name = serializers.SerializerMethodField(read_only=True)
    role = serializers.ChoiceField(choices=UserTypeChoices.choices, read_only=True)
    teams = TeamSerializer(many=True, read_only=True)

    def get_avatar(self, obj):
        return obj.avatar.url if obj.avatar else settings.STATIC_URL + 'images/default_avatar.png'

    def get_status(self, obj):
        return "active" if obj.is_active else "inactive"

    def get_full_name(self, obj):
        return obj.full_name

    def get_short_name(self, obj):
        return obj.short_name

    class Meta:
        model = User
        fields = [
            "id",
            'email',
            'avatar',
            'status',
            'first_name',
            'last_name',
            'full_name',
            'short_name',
            'registered_at',
            'is_active',
            'role',
            'teams',
        ]


class UserWriteSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)

    # teams = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
