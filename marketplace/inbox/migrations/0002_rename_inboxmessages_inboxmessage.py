# Generated by Django 5.0.4 on 2024-05-20 16:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InboxMessages',
            new_name='InboxMessage',
        ),
    ]
