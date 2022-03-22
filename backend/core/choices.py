from django.db import models
from django.utils.translation import gettext as _


# RES: https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.Field.choices
class UserTypeChoices(models.TextChoices):
    EMPLOYEE = 'employee', _('Employee')
    ADMIN = 'admin', _('Admin')


# RES: https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.Field.choices
class SpotIssueStatusChoices(models.TextChoices):
    SUBMITTED = 'submitted', _('Submitted')
    OPEN = 'open', _('Open')
    IN_PROGRESS = 'in_progress', _('In progress')
    RESOLVED = 'resolved', _('Resolved')


class SpotStatusChoices(models.TextChoices):
    AVAILABLE = 'available', _('Available')
    NOT_AVAILABLE = 'not_available', _('Not available')
    BOOKED_FOR_USER = 'booked_for_user', _('Booked by user')
    BOOKED_FOR_TEAM = 'booked_for_team', _('Booked by team')
    BOOKED_PERMANENTLY = 'booked_permanently', _('Booked permanently')
