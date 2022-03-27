from django.db import models
from polymorphic.models import PolymorphicModel

from apps.teams.models import Team
from apps.users.models import User
from apps.workspaces.models import Spot


class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_reservations', on_delete=models.DO_NOTHING)
    datetime_from = models.DateTimeField()
    datetime_to = models.DateTimeField()

    def __str__(self):
        return f'from {self.datetime_from.strftime("%d.%m-%H:%M")} to {self.datetime_to.strftime("%d.%m-%H:%M")}'


class SpotReservation(PolymorphicModel):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_spot_reservations', on_delete=models.DO_NOTHING)
    reservation = models.OneToOneField(Reservation, related_name='reservations_for_spot', on_delete=models.CASCADE)
    # TODO many to many
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE)
    permanent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.spot} - {self.reservation}"


class UserSpotReservation(SpotReservation):
    reservation_for = models.ForeignKey(User, related_name='user_reservations_for_spot', on_delete=models.CASCADE)


class TeamSpotReservation(SpotReservation):
    reservation_for = models.ForeignKey(Team, related_name='team_reservations_for_spot', on_delete=models.CASCADE)
