# Generated by Django 5.2 on 2025-05-08 22:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book_copy', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('rental_id', models.AutoField(primary_key=True, serialize=False)),
                ('borrow_date', models.DateField()),
                ('expected_date', models.DateField()),
                ('actual_date', models.DateField(blank=True, null=True)),
                ('copy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rentals', to='book_copy.bookcopy')),
                ('cust', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rentals', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'AYT_RENTAL',
                'constraints': [models.CheckConstraint(condition=models.Q(('expected_date__gt', models.F('borrow_date'))), name='check_borrow_date')],
                'unique_together': {('cust', 'copy', 'borrow_date')},
            },
        ),
    ]
