from requests import Response
from rest_framework import viewsets
from rest_framework.decorators import action

from apps.reservations.api.serializers import SpotReservationSerializer, SpotSerializer
from apps.reservations.models import SpotReservation
from apps.workspaces.models import Spot


class SpotViewSet(viewsets.ModelViewSet):
    serializer_class = SpotSerializer
    queryset = Spot.objects.all()

    @action(detail=True, methods=['post', 'delete'])
    def reservations(self, request, pk=None):
        return Response({'status': 'okeeej set'})


class SpotReservationViewSet(viewsets.ModelViewSet):
    serializer_class = SpotReservationSerializer
    queryset = SpotReservation.objects.all()
