# Generated by Django 5.2 on 2025-05-07 07:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("room", "0003_room_image_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="image_url",
            field=models.URLField(blank=True, null=True),
        ),
    ]
