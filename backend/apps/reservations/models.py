from django.db import models

from apps.users.models import User


class Reservation(models.Model):
    created_by = models.ForeignKey(User, related_name='created_reservation', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
