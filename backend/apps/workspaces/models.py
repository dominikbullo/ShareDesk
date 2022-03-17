from django.db import models

from apps.users.models import User


class Workspace(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    # created_by = models.ForeignKey(User, related_name='created_worskspaces', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)


class Layout(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    # created_by = models.ForeignKey(User, related_name='created_layouts', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)


class Room(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    # created_by = models.ForeignKey(User, related_name='created_rooms', on_delete=models.DO_NOTHING)
    position = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    layout = models.ForeignKey(Layout, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class Spot(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    # created_by = models.ForeignKey(User, related_name='created_spot', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    position = models.ForeignKey(Room, on_delete=models.CASCADE)


class SpotIssue(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    # created_by = models.ForeignKey(User, related_name='created_spot_issues', on_delete=models.DO_NOTHING)
    spot = models.OneToOneField(Spot, on_delete=models.CASCADE)
    description = models.TextField()
