from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer

from apps.reservations.models import UserSpotReservation, TeamSpotReservation, Reservation, SpotReservation
from apps.teams.api.serializers import TeamSerializer
from apps.users.api.serializers import UserSerializer
from apps.workspaces.api.serializers import SpotSerializer


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"


class SpotReservationSerializer(serializers.ModelSerializer):
    reservation = ReservationSerializer()

    def validate(self, attrs):
        print("validate")
        # Daj rezervacie od do času kde spot je spot ktorý chcem save a check či exist, ak hej validate error
        # if reservation.datetime_from
        # reservation.datetime_to
        reservation_start = attrs["reservation"]["start"]
        reservation_end = attrs["reservation"]["end"]

        # same_spot_and_time = SpotReservation.objects.filter(reservation__datetime_from__gte=reservation_from,
        #                                                     reservation__datetime__to__lte=reservation_to,
        #                                                     spots__in=attrs["spots"])
        # if same_spot_and_time.exists():
        #     raise serializers.ValidationError("Seat already booked for this time")

        return super().validate(attrs)

    def to_representation(self, instance):
        self.fields["reservation"] = ReservationSerializer(read_only=True)
        self.fields["spots"] = SpotSerializer(read_only=True, many=True)
        to_representation = super().to_representation(instance)
        return to_representation


class SpotReservationByUserSerializer(SpotReservationSerializer):

    def create(self, validated_data):
        reservation_data = validated_data.pop('reservation')
        spots = validated_data.pop('spots')
        reservation = Reservation.objects.create(**reservation_data)
        instance = UserSpotReservation.objects.create(**validated_data, reservation=reservation)
        instance.spots.set(spots)
        return instance

    def to_representation(self, instance):
        self.fields["reservation_for"] = UserSerializer(read_only=True)
        to_representation = super().to_representation(instance)
        return to_representation

    class Meta:
        model = UserSpotReservation
        fields = "__all__"


class SpotReservationByTeamSerializer(SpotReservationSerializer):

    def create(self, validated_data):
        reservation_data = validated_data.pop('reservation')
        spots = validated_data.pop('spots')
        reservation = Reservation.objects.create(**reservation_data)
        instance = TeamSpotReservation.objects.create(**validated_data, reservation=reservation)
        instance.spots.set(spots)
        return instance

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
