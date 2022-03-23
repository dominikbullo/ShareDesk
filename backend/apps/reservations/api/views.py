from rest_framework import viewsets

from apps.reservations.api.serializers import EventPolymorphicSerializer
from apps.reservations.models import SpotReservation


class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = EventPolymorphicSerializer
    queryset = SpotReservation.objects.all()
    filterset_fields = "__all__"
