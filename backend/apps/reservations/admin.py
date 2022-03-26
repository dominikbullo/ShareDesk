from django.contrib import admin
from django.contrib.admin.decorators import display
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
    list_filter = ("reservation", "permanent",)
    list_display = PolymorphicParentModelAdmin.list_display + \
                   ("reservation", "permanent", "get_room", "get_floor", "get_workspace")

    @display(ordering='spot__room', description='Room')
    def get_room(self, obj):
        return obj.spot.room

    @display(ordering='spot__room__floor', description='Floor')
    def get_floor(self, obj):
        return obj.spot.room.floor

    @display(ordering='spot__room__floor__workspace', description='Workspace')
    def get_workspace(self, obj):
        return obj.spot.room.floor.workspace
