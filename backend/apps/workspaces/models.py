from django.db import models

from apps.users.models import User


class RoomLayout(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    # created_by = models.ForeignKey(User, related_name='created_layouts', on_delete=models.DO_NOTHING)
    rows = models.IntegerField()
    columns = models.IntegerField()
    name = models.CharField(max_length=255)


# class FloorLayout(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     # created_by = models.ForeignKey(User, related_name='created_layouts', on_delete=models.DO_NOTHING)
#     name = models.CharField(max_length=255)


class Workspace(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    # created_by = models.ForeignKey(User, related_name='created_worskspaces', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)


class Floor(models.Model):
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    floor_number = models.IntegerField()
    name = models.CharField(max_length=255)


# class FloorPlan(models.Model):
#     floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)


class Room(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    layout = models.ForeignKey(RoomLayout, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255, blank=True, null=True)


class Spot(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    row = models.IntegerField()
    column = models.IntegerField()
    enabled = models.BooleanField(default=True)
    name = models.CharField(max_length=255)


class SpotIssue(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    # created_by = models.ForeignKey(User, related_name='created_spot_issues', on_delete=models.DO_NOTHING)
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE)
    description = models.TextField()
