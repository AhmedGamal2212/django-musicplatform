# Generated by Django 4.1.2 on 2022-10-30 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_customuser_bio"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="bio",
            field=models.CharField(blank=True, default="", max_length=256),
        ),
    ]
