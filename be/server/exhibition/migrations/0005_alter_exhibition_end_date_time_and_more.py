# Generated by Django 5.2 on 2025-05-13 04:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("exhibition", "0004_alter_exhibition_end_date_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exhibition",
            name="end_date_time",
            field=models.DateTimeField(
                default=datetime.datetime(2025, 5, 23, 0, 28, 12, 257151)
            ),
        ),
        migrations.AlterField(
            model_name="exhibition",
            name="start_date_time",
            field=models.DateTimeField(
                default=datetime.datetime(2025, 5, 13, 0, 28, 12, 257113)
            ),
        ),
    ]
