# Generated by Django 3.2.6 on 2021-12-26 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_tempwallet_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='tempwallet',
            name='money_before_edit',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
