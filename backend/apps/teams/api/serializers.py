from rest_framework import serializers

from apps.teams.models import Team


class TeamSerializer(serializers.ModelSerializer):
    # created_by = UserSerializer(default=serializers.CurrentUserDefault())
    members_count = serializers.SerializerMethodField()

    def get_members_count(self, obj):
        return Team.objects.get(id=obj.id).members.all().count()

    class Meta:
        model = Team
        fields = "__all__"
        read_only_fields = ['created_by']
