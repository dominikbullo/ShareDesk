# Generated by Django 4.0.3 on 2022-03-27 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0005_remove_spotreservation_spot_spotreservation_spots'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spotreservation',
            old_name='spots',
            new_name='spot',
        ),
    ]