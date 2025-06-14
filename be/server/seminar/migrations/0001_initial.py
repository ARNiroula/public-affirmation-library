# Generated by Django 5.2 on 2025-05-07 21:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seminar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keynote_speaker', models.CharField(max_length=100)),
                ('seminar_type', models.CharField(max_length=50)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seminars', to='event.event')),
            ],
            options={
                'db_table': 'AYT_SEMINAR',
            },
        ),
    ]
