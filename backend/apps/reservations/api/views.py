from rest_framework import viewsets

from apps.reservations.api.serializers import SpotReservationSerializer
from apps.reservations.models import SpotReservation


class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = SpotReservationSerializer
    queryset = SpotReservation.objects.all()
