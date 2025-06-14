# Generated by Django 5.2 on 2025-05-13 05:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("seminar", "0004_alter_seminar_end_date_time_and_more"),
        ("sponser", "0003_sponser_sponsor_type_alter_sponser_lname"),
    ]

    operations = [
        migrations.AddField(
            model_name="seminar",
            name="image_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="seminar",
            name="sponser",
            field=models.ManyToManyField(
                related_name="seminar",
                through="sponser.SponserSeminarRelationship",
                to="sponser.sponser",
            ),
        ),
        migrations.AlterField(
            model_name="seminar",
            name="end_date_time",
            field=models.DateTimeField(
                default=datetime.datetime(2025, 5, 23, 1, 3, 33, 688356)
            ),
        ),
        migrations.AlterField(
            model_name="seminar",
            name="start_date_time",
            field=models.DateTimeField(
                default=datetime.datetime(2025, 5, 13, 1, 3, 33, 688319)
            ),
        ),
    ]
