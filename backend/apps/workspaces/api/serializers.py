from rest_framework import serializers

from apps.workspaces.models import Workspace, SpotIssue, Spot


class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = "__all__"


class SpotIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotIssue
        fields = "__all__"


class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = "__all__"
