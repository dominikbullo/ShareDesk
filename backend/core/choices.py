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


class SpotPermanentStatusChoices(models.TextChoices):
    SUBMITTED = 'submitted', _('Submitted')
    ALLOWED = 'allowed', _('Allowed')
    REJECTED = 'rejected', _('Rejected')
