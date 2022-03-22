from django.db import models

from apps.users.models import User
from core.choices import SpotIssueStatusChoices


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

    def __str__(self):
        return self.name


class Floor(models.Model):
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    number = models.IntegerField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.number}"


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

    def __str__(self):
        if self.number:
            return f"room {self.number}"
        return f"room on {self.floor}."

    def spot_number(self):
        if self.number:
            return self.number
        return "No identification"


class Spot(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    enabled = models.BooleanField(default=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    row = models.IntegerField()
    column = models.IntegerField()
    identifier = models.CharField(max_length=255)

    def __str__(self):
        return f"spot {self.identifier}"


class SpotIssue(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    # created_by = models.ForeignKey(User, related_name='created_spot_issues', on_delete=models.DO_NOTHING)
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=SpotIssueStatusChoices.choices,
        default=SpotIssueStatusChoices.SUBMITTED
    )

    def __str__(self):
        return f"{self.subject} at {self.spot}"
