from django.db import models

from apps.users.models import User


class Workspace(models.Model):
    created_by = models.ForeignKey(User, related_name='created_worskapces', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
