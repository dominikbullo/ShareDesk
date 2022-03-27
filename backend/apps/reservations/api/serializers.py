from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer

from apps.reservations.models import UserSpotReservation, TeamSpotReservation, Reservation
from apps.teams.api.serializers import TeamSerializer
from apps.users.api.serializers import UserSerializer
from apps.workspaces.api.serializers import SpotSerializer


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"


class SpotReservationSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        self.fields["reservation"] = ReservationSerializer(read_only=True)
        self.fields["spots"] = SpotSerializer(read_only=True, many=True)
        to_representation = super().to_representation(instance)
        return to_representation


class SpotReservationByUserSerializer(SpotReservationSerializer):

    def to_representation(self, instance):
        self.fields["reservation_for"] = UserSerializer(read_only=True)
        to_representation = super().to_representation(instance)
        return to_representation

    class Meta:
        model = UserSpotReservation
        fields = "__all__"


class SpotReservationByTeamSerializer(SpotReservationSerializer):
    def to_representation(self, instance):
        self.fields["reservation_for"] = TeamSerializer(read_only=True)
        to_representation = super().to_representation(instance)
        return to_representation

    class Meta:
        model = TeamSpotReservation
        fields = "__all__"


class SpotReservationPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        UserSpotReservation: SpotReservationByUserSerializer,
        TeamSpotReservation: SpotReservationByTeamSerializer,
    }
