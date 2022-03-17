from django.db import models

from apps.users.models import User


class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
