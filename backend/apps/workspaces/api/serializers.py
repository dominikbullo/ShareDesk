from rest_framework import serializers

from apps.workspaces.models import Workspace, SpotIssue, Spot, Floor, Room, RoomLayout
from core.choices import SpotIssueStatusChoices


class RoomLayoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomLayout
        fields = "__all__"


class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = "__all__"


class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    layout = RoomLayoutSerializer()
    spots = serializers.SerializerMethodField()
    workspace = serializers.SerializerMethodField()

    def get_workspace(self, obj):
        return obj.floor.workspace.id

    def get_spots(self, obj):
        return SpotSerializer(Spot.objects.filter(room_id=obj.id), many=True).data

    class Meta:
        model = Room
        fields = "__all__"


class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = "__all__"


class SpotIssueSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=SpotIssueStatusChoices.choices,
                                     default=SpotIssueStatusChoices.SUBMITTED,
                                     allow_null=True)

    class Meta:
        model = SpotIssue
        fields = "__all__"
