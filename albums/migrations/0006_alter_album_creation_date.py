# Generated by Django 4.1.2 on 2022-10-18 16:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0005_alter_album_creation_date_alter_album_is_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 18, 16, 10, 12, 240248, tzinfo=datetime.timezone.utc), editable=False, verbose_name='creation date'),
        ),
    ]
