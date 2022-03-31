from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.workspaces.models import Room, Spot

from django.db.models.signals import pre_save


# @receiver(pre_save, sender=SpotReservation)
# def ensure_reservation_is_unique(sender, instance, using):
#     if not instance.subject_init:
#         instance.subject_init = instance.subject_initials()


@receiver(post_save, sender=Room)
def room_post_save_handler(sender, instance, created, **kwargs):
    if created:
        # https://stackoverflow.com/questions/48768148/create-multiple-django-model-instances-using-for-loop
        spots = []
        for row in range(1, instance.layout.rows + 1):
            for column in range(1, instance.layout.columns + 1):
                data = {
                    "enabled": True,
                    "room": instance,
                    "row": row,
                    "column": column,
                }
                if not Spot.objects.filter(**data).exists():
                    data["identifier"] = f"S[{row}-{column}]"
                    spots.append(Spot(**data))
        Spot.objects.bulk_create(spots)
