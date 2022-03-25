# Generated by Django 4.0.3 on 2022-03-25 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_remove_spotreservation_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotreservation',
            name='reservation',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='reservations_for_spot', to='reservations.reservation'),
        ),
    ]
