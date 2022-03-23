# Generated by Django 4.0.3 on 2022-03-22 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspaces', '0008_spotissue_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='spot',
            name='status',
            field=models.CharField(choices=[('available', 'Available'), ('not_available', 'Not available'), ('booked_for_user', 'Booked by user'), ('booked_for_team', 'Booked by team'), ('booked_permanently', 'Booked permanently')], default='available', max_length=20),
        ),
    ]