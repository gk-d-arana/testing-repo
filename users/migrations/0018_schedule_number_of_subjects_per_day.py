# Generated by Django 3.2.6 on 2021-12-31 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20211231_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='number_of_subjects_per_day',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
