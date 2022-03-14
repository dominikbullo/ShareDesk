from rest_framework import serializers

from apps.teams.models import Team


class TeamSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)

    class Meta:
        model = Team
        fields = "__all__"
