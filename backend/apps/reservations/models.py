from django.db import models

from apps.users.models import User
from apps.workspaces.models import Spot


class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_reservations', on_delete=models.DO_NOTHING)
    datetime_from = models.DateTimeField()
    datetime_to = models.DateTimeField()


class SpotReservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_spot_reservations', on_delete=models.DO_NOTHING)
    reservation_for = models.ForeignKey(User, related_name='user_reservations_for_spot', on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, related_name='reservations_for_spot', on_delete=models.CASCADE)
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE)
    permanent = models.BooleanField(default=False)
    # Don't need frequency - 2 sceneries
    # Book for reservation time, or permanent, from reservation time start for everyday
    # frequency = models.IntegerField(blank=True, null=True)
