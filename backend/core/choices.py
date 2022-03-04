from django.db import models
from django.utils.translation import gettext as _


# RES: https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.Field.choices
class UserTypeChoices(models.TextChoices):
    EMPLOYEE = 'employee', _('Employee')
    ADMIN = 'admin', _('Admin')
