# Generated by Django 3.2.6 on 2021-12-26 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20211227_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='tempwallet',
            name='number',
            field=models.CharField(blank=True, default=0, max_length=255, null=True),
        ),
    ]
