# Generated by Django 3.2.6 on 2021-12-12 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20211212_0222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mylearning',
            name='progress',
        ),
    ]
