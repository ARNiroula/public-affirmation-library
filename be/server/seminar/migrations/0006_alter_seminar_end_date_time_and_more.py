# Generated by Django 5.2 on 2025-05-13 05:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("seminar", "0005_seminar_image_url_seminar_sponser_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="seminar",
            name="end_date_time",
            field=models.DateTimeField(
                default=datetime.datetime(2025, 5, 23, 1, 56, 43, 578156)
            ),
        ),
        migrations.AlterField(
            model_name="seminar",
            name="start_date_time",
            field=models.DateTimeField(
                default=datetime.datetime(2025, 5, 13, 1, 56, 43, 578120)
            ),
        ),
    ]
