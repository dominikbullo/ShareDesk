from rest_framework import viewsets

from apps.workspaces.api.serializers import WorkspaceSerializer
from apps.workspaces.models import Workspace


class WorkspaceViewSet(viewsets.ModelViewSet):
    serializer_class = WorkspaceSerializer
    queryset = Workspace.objects.all()
