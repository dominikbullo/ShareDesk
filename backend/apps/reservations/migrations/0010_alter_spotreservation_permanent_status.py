# Generated by Django 4.0.3 on 2022-03-30 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0009_alter_spotreservation_permanent_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotreservation',
            name='permanent_status',
            field=models.CharField(blank=True, choices=[('submitted', 'Submitted'), ('allowed', 'Allowed'), ('rejected', 'Rejected')], default='submitted', max_length=20, null=True),
        ),
    ]
