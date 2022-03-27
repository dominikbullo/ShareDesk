from django.db.models import Q
from django_filters import rest_framework as django_filters
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.reservations.api.serializers import SpotReservationPolymorphicSerializer
from apps.reservations.models import SpotReservation, UserSpotReservation, TeamSpotReservation
from apps.teams.models import Team
from apps.workspaces.models import Room


class ReservationFilter(django_filters.FilterSet):
    room = django_filters.ModelChoiceFilter(
        label='Room',
        empty_label='All rooms',
        queryset=Room.objects.all(),
        to_field_name="id",
        method='filter_room',
    )

    # https://stackoverflow.com/questions/30366564/daterange-on-a-django-filter
    reservation_start = django_filters.DateTimeFilter(field_name="reservation__datetime_from__date",
                                                      lookup_expr=('lte'), )
    reservation_end = django_filters.DateTimeFilter(field_name="reservation__datetime_to__date", lookup_expr=('gte'), )

    def filter_room(self, queryset, name, value):
        return queryset.filter(spot__room_id=value.id)

    class Meta:
        model = SpotReservation
        fields = "__all__"


class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = SpotReservationPolymorphicSerializer
    queryset = SpotReservation.objects.all()
    filterset_class = ReservationFilter

    @action(methods=['GET'], detail=False)
    def my_reservations(self, request):
        # https://django-polymorphic.readthedocs.io/en/stable/advanced.html
        # https://stackoverflow.com/questions/59476948/filtering-a-many-to-many-relationship-with-djangos-q-query
        user_reservations = SpotReservation.objects.filter(Q(UserSpotReservation___reservation_for=request.user))
        user_team_reservations = SpotReservation.objects.filter(
            Q(TeamSpotReservation___reservation_for__in=Team.objects.filter(user=request.user)))
        queryset = user_reservations | user_team_reservations
        serializer = self.serializer_class(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
