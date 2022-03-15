from rest_framework import serializers

from apps.reservations.models import SpotReservation
from apps.workspaces.models import Spot


class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = "__all__"


class SpotReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotReservation
        fields = "__all__"
