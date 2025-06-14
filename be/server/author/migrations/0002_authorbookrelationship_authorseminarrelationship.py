# Generated by Django 5.2 on 2025-05-07 21:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
        ('book', '0001_initial'),
        ('seminar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorBookRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='author.author')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book')),
            ],
        ),
        migrations.CreateModel(
            name='AuthorSeminarRelationship',
            fields=[
                ('invitation_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='author.author')),
                ('seminar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seminar.seminar')),
            ],
        ),
    ]
