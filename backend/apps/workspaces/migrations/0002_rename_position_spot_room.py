# Generated by Django 4.0.3 on 2022-03-18 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workspaces', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spot',
            old_name='position',
            new_name='room',
        ),
    ]
