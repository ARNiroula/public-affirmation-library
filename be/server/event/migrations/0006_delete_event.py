# Generated by Django 5.2 on 2025-05-13 04:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("event", "0005_remove_event_check_datetime_order_and_more"),
        ("exhibition", "0003_remove_exhibition_event_remove_exhibition_id_and_more"),
        ("seminar", "0002_remove_seminar_event_remove_seminar_id_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Event",
        ),
    ]
