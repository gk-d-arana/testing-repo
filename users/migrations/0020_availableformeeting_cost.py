# Generated by Django 3.2.6 on 2021-12-31 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20211231_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='availableformeeting',
            name='cost',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
