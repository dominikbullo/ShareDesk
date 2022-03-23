from rest_framework import serializers

from apps.workspaces.models import Workspace, SpotIssue, Spot, Floor, Room


class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = "__all__"


class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = "__all__"


class SpotIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotIssue
        fields = "__all__"
