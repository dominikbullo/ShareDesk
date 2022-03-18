from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered
from polymorphic.admin import PolymorphicChildModelAdmin, PolymorphicParentModelAdmin

from apps.reservations.models import Reservation, SpotReservation, TeamSpotReservation, UserSpotReservation


class HideFromMenuAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False


# admin.site.unregister(Reservation)
admin.site.register(Reservation, HideFromMenuAdmin)


@admin.register(UserSpotReservation)
class UserSpotReservationAdmin(PolymorphicChildModelAdmin):
    base_model = UserSpotReservation


@admin.register(TeamSpotReservation)
class TeamSpotReservationAdmin(PolymorphicChildModelAdmin):
    base_model = TeamSpotReservation


@admin.register(SpotReservation)
class SpotReservationAdmin(PolymorphicParentModelAdmin):
    base_model = SpotReservation
    child_models = (UserSpotReservation, TeamSpotReservation)
