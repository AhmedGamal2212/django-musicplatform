# Generated by Django 4.1.2 on 2022-10-18 19:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0006_alter_album_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 18, 19, 3, 43, 160952, tzinfo=datetime.timezone.utc), editable=False, verbose_name='creation date'),
        ),
    ]
