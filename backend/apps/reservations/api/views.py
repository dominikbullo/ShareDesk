from rest_framework import viewsets

from apps.reservations.api.serializers import ReservationSerializer
from apps.reservations.models import Reservation


class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()
