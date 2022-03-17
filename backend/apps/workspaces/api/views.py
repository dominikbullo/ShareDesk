from requests import Response
from rest_framework import viewsets
from rest_framework.decorators import action

from apps.workspaces.api.serializers import WorkspaceSerializer, SpotIssueSerializer, SpotSerializer
from apps.workspaces.models import Workspace, SpotIssue, Spot


class SpotIssueViewSet(viewsets.ModelViewSet):
    serializer_class = SpotIssueSerializer
    queryset = SpotIssue.objects.all()
    filterset_fields = "__all__"


class WorkspaceViewSet(viewsets.ModelViewSet):
    serializer_class = WorkspaceSerializer
    queryset = Workspace.objects.all()
    filterset_fields = "__all__"


class SpotViewSet(viewsets.ModelViewSet):
    serializer_class = SpotSerializer
    queryset = Spot.objects.all()

    @action(detail=True, methods=['post', 'delete'])
    def reservations(self, request, pk=None):
        return Response({'status': 'okeeej set'})
