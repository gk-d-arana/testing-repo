# Generated by Django 3.2.6 on 2021-12-12 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_auto_20211207_1733'),
        ('users', '0005_auto_20211207_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='mylearning',
            name='progress',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.CreateModel(
            name='MyLearningCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_watched', models.BooleanField(default=False)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='my_learning_course', to='courses.course')),
            ],
        ),
        migrations.AlterField(
            model_name='mylearning',
            name='courses',
            field=models.ManyToManyField(blank=True, to='users.MyLearningCourse'),
        ),
    ]
