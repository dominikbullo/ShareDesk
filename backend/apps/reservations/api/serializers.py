from rest_framework import serializers

from apps.reservations.models import SpotReservation


class SpotReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotReservation
        fields = "__all__"
