# Generated by Django 4.0.3 on 2022-03-18 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspaces', '0004_remove_room_columns_remove_room_rows_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spot',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
    ]
