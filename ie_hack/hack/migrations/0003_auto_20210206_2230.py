# Generated by Django 3.0.11 on 2021-02-06 22:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hack', '0002_auto_20210206_2141'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Request',
            new_name='EventRequest',
        ),
    ]
