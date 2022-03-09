from django.db import models

from apps.users.models import User


class Team(models.Model):
    title = models.CharField(max_length=255)
    members = models.ManyToManyField(User, through=User.teams.through, blank=True)
    # members = models.ManyToManyField(User, related_name='teams')
    created_by = models.ForeignKey(User, related_name='created_teams', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
