# Generated by Django 4.0.3 on 2022-03-30 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0011_remove_reservation_created_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='datetime_to',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='datetime_from',
            new_name='start',
        ),
    ]
