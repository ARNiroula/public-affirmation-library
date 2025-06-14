# Generated by Django 5.2 on 2025-05-09 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponser', '0002_alter_sponser_sponser_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponser',
            name='sponsor_type',
            field=models.CharField(choices=[('I', 'Individual'), ('O', 'Organization')], default='I', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sponser',
            name='lname',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
