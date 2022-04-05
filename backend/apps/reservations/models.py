from django.db import models
from polymorphic.models import PolymorphicModel

from apps.teams.models import Team
from apps.users.models import User
from apps.workspaces.models import Spot
from core.choices import SpotPermanentStatusChoices


# class Settings(models.Model):
#     reservation_start_time = models.TimeField(default='8:00')
#     reservation_end_time = models.TimeField(default='8:00')


class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    # created_by = models.ForeignKey(User, related_name='created_reservations', on_delete=models.DO_NOTHING)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return f'from {self.start.strftime("%d.%m-%H:%M")} to {self.end.strftime("%d.%m-%H:%M")}'


class SpotReservation(PolymorphicModel):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_spot_reservations', on_delete=models.DO_NOTHING)
    reservation = models.OneToOneField(Reservation, related_name='reservations_for_spot', on_delete=models.CASCADE)
    spots = models.ManyToManyField(Spot)
    permanent = models.BooleanField(default=False)
    permanent_status = models.CharField(
        blank=True, null=True,
        max_length=20,
        choices=SpotPermanentStatusChoices.choices,
        default=SpotPermanentStatusChoices.SUBMITTED
    )

    def __str__(self):
        return f"{self.reservation}"

    def get_spots(self):
        return "\n".join([str(p) for p in self.spots.all()])


class UserSpotReservation(SpotReservation):
    reservation_for = models.ForeignKey(User, related_name='user_reservations_for_spot', on_delete=models.CASCADE)


class TeamSpotReservation(SpotReservation):
    reservation_for = models.ForeignKey(Team, related_name='team_reservations_for_spot', on_delete=models.CASCADE)
