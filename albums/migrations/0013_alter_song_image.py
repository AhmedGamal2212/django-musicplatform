# Generated by Django 4.1.2 on 2022-10-28 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("albums", "0012_alter_song_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="song",
            name="image",
            field=models.ImageField(blank=True, upload_to="song-images"),
        ),
    ]
