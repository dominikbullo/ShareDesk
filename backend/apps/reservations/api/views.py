from django_filters import rest_framework as django_filters, widgets
from django_filters.widgets import RangeWidget
from rest_framework import viewsets

from apps.reservations.api.serializers import EventPolymorphicSerializer
from apps.reservations.models import SpotReservation
from apps.workspaces.models import Room


class ReservationFilter(django_filters.FilterSet):
    workspace = django_filters.ModelChoiceFilter(
        label='Room',
        empty_label='All rooms',
        queryset=Room.objects.all(),
        to_field_name="id",
        method='filter_room',
    )

    # https://stackoverflow.com/questions/30366564/daterange-on-a-django-filter
    reservation_start = django_filters.DateTimeFilter(field_name="reservation__datetime_from", lookup_expr=('gt'), )
    reservation_end = django_filters.DateTimeFilter(field_name="reservation__datetime_to", lookup_expr=('lt'), )

    def filter_room(self, queryset, name, value):
        return queryset.filter(spot__room_id=value.id)

    class Meta:
        model = SpotReservation
        fields = "__all__"


class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = EventPolymorphicSerializer
    queryset = SpotReservation.objects.all()
    filterset_class = ReservationFilter
