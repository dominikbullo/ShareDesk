from django_filters import rest_framework as django_filters
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.reservations.api.serializers import SpotReservationPolymorphicSerializer
from apps.reservations.models import SpotReservation
from apps.workspaces.api.serializers import WorkspaceSerializer, SpotIssueSerializer, SpotSerializer, FloorSerializer, \
    RoomSerializer, RoomLayoutSerializer
from apps.workspaces.models import Workspace, SpotIssue, Spot, Floor, Room, RoomLayout


class RoomLayoutViewSet(viewsets.ModelViewSet):
    serializer_class = RoomLayoutSerializer
    queryset = RoomLayout.objects.all()
    filterset_fields = "__all__"


class WorkspaceViewSet(viewsets.ModelViewSet):
    serializer_class = WorkspaceSerializer
    queryset = Workspace.objects.all()
    filterset_fields = "__all__"


class FloorViewSet(viewsets.ModelViewSet):
    serializer_class = FloorSerializer
    queryset = Floor.objects.all()
    filterset_fields = "__all__"


class RoomFilter(django_filters.FilterSet):
    workspace = django_filters.ModelChoiceFilter(
        label='Workspace',
        empty_label='All workspaces',
        queryset=Workspace.objects.all(),
        to_field_name="id",
        method='filter_workspace',
    )

    def filter_workspace(self, queryset, name, value):
        return queryset.filter(floor__workspace_id=value.id)

    class Meta:
        model = Room
        fields = "__all__"


class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    filterset_class = RoomFilter


class SpotIssueViewSet(viewsets.ModelViewSet):
    serializer_class = SpotIssueSerializer
    queryset = SpotIssue.objects.all()
    filterset_fields = "__all__"


class SpotViewSet(viewsets.ModelViewSet):
    serializer_class = SpotSerializer
    queryset = Spot.objects.all()

    # I dont need this for now
    # @action(detail=True, methods=['GET'])
    # def reservations(self, request, pk=None):
    #     queryset = SpotReservation.objects.filter(spot=pk)
    #     serializer = SpotReservationPolymorphicSerializer(queryset, many=True)
    #     return Response(status=status.HTTP_200_OK, data=serializer.data)
