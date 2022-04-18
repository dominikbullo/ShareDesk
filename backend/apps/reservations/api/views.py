from django.db.models import Q
from django_filters import rest_framework as django_filters
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.reservations.api.serializers import SpotReservationPolymorphicSerializer, ReservationSerializer
from apps.reservations.models import SpotReservation, UserSpotReservation, TeamSpotReservation, Reservation
from apps.teams.models import Team
from apps.workspaces.models import Room, Spot
from core.choices import SpotPermanentStatusChoices
from core.permissions import IsAdminOrReadOnly


class ReservationFilter(django_filters.FilterSet):
    room = django_filters.ModelChoiceFilter(
        label='Room',
        empty_label='All rooms',
        queryset=Room.objects.all(),
        to_field_name="id",
        method='filter_room',
    )
    reservation_start = django_filters.DateTimeFilter(field_name="reservation__start__date",
                                                      lookup_expr=('lte'), )
    reservation_end = django_filters.DateTimeFilter(field_name="reservation__end__date", lookup_expr=('gte'), )

    def filter_room(self, queryset, name, value):
        return queryset.filter(spots__room_id=value)

    class Meta:
        model = SpotReservation
        fields = "__all__"


class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = SpotReservationPolymorphicSerializer
    queryset = SpotReservation.objects.all()
    filterset_class = ReservationFilter

    @action(methods=['GET'], detail=False, url_path='my-reservations')
    def my_reservations(self, request):
        # https://django-polymorphic.readthedocs.io/en/stable/advanced.html
        # https://stackoverflow.com/questions/59476948/filtering-a-many-to-many-relationship-with-djangos-q-query
        user_reservations = SpotReservation.objects.filter(Q(UserSpotReservation___reservation_for=request.user))
        user_team_reservations = SpotReservation.objects.filter(
            Q(TeamSpotReservation___reservation_for__in=Team.objects.filter(user=request.user)))
        queryset = user_reservations | user_team_reservations
        serializer = self.serializer_class(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(methods=['POST'], detail=True, url_path='change-status', permission_classes=[IsAdminOrReadOnly])
    def change_status(self, request, pk=None):
        reservation = self.get_object()
        new_status = request.data.get('status', None)
        if new_status not in SpotPermanentStatusChoices:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        reservation.permanent_status = new_status
        reservation.save()
        return Response(data=self.serializer_class(reservation).data, status=status.HTTP_200_OK)
