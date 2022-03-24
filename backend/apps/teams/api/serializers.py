from rest_framework import serializers

from apps.teams.models import Team


class TeamSerializer(serializers.ModelSerializer):
    # created_by = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
    members_count = serializers.SerializerMethodField()

    def get_members_count(self, obj):
        return Team.objects.get(id=obj.id).members.all().count()

    class Meta:
        model = Team
        fields = "__all__"
