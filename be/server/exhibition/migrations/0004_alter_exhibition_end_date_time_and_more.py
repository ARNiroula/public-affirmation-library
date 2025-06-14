# Generated by Django 5.2 on 2025-05-13 04:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("exhibition", "0003_remove_exhibition_event_remove_exhibition_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exhibition",
            name="end_date_time",
            field=models.DateTimeField(
                default=datetime.datetime(2025, 5, 23, 0, 27, 28, 565706)
            ),
        ),
        migrations.AlterField(
            model_name="exhibition",
            name="event_topic",
            field=models.CharField(
                choices=[
                    ("LIT", "Literature & Author Talks"),
                    ("HIS", "History & Archives"),
                    ("SCI", "Science & Nature"),
                    ("ART", "Art Exhibitions & Workshops"),
                    ("MUS", "Music & Performance"),
                    ("TEC", "Technology & Innovation"),
                    ("EDU", "Education & Learning Skills"),
                    ("WRIT", "Creative Writing"),
                    ("CHD", "Children’s Programs"),
                    ("YTH", "Youth & Teen Engagement"),
                    ("CUL", "Cultural Heritage"),
                    ("COM", "Community & Social Issues"),
                    ("ENV", "Environment & Sustainability"),
                    ("HLTH", "Health & Wellness"),
                    ("DIG", "Digital Literacy"),
                    ("FILM", "Film Screenings & Analysis"),
                    ("PHI", "Philosophy & Ethics"),
                    ("BIZ", "Business & Career Development"),
                    ("DIY", "DIY, Crafts & Makerspaces"),
                    ("LANG", "Language & Literacy"),
                ],
                db_index=True,
                default="LIT",
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="exhibition",
            name="start_date_time",
            field=models.DateTimeField(
                default=datetime.datetime(2025, 5, 13, 0, 27, 28, 565668)
            ),
        ),
        migrations.AlterField(
            model_name="exhibition",
            name="topic_bitmap",
            field=models.BigIntegerField(db_index=True, default=0, editable=False),
        ),
    ]
