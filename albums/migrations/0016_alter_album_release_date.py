# Generated by Django 4.1.2 on 2022-11-03 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("albums", "0015_alter_song_audio_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="album",
            name="release_date",
            field=models.DateTimeField(blank=True, verbose_name="release date"),
        ),
    ]
