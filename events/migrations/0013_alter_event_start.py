# Generated by Django 4.1 on 2023-06-22 00:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_alter_event_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 22, 0, 30, 22, 204075, tzinfo=datetime.timezone.utc)),
        ),
    ]
