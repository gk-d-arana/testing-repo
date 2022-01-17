# Generated by Django 3.2.6 on 2022-01-17 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        ('extras', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mytest',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.instructor'),
        ),
        migrations.AddField(
            model_name='mytest',
            name='my_edot_ques_answers',
            field=models.ManyToManyField(to='courses.MyEditorialQuestion'),
        ),
        migrations.AddField(
            model_name='mytest',
            name='my_multi_choice_ques_answers',
            field=models.ManyToManyField(to='courses.MyMultipleChoiceQuestion'),
        ),
        migrations.AddField(
            model_name='mymultiplechoicequestion',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.multiplechoicequestion'),
        ),
        migrations.AddField(
            model_name='myeditorialquestion',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.editorialquestion'),
        ),
        migrations.AddField(
            model_name='multiplechoicequestion',
            name='answers',
            field=models.ManyToManyField(blank=True, to='courses.Answer'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meeting_instructor', to='users.instructor'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='students',
            field=models.ManyToManyField(blank=True, to='users.Instructor'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='courses.video'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_enrolled', to='courses.course'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='user_enrolling',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_enrolling', to='users.instructor'),
        ),
        migrations.AddField(
            model_name='coursetest',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='extras.category'),
        ),
        migrations.AddField(
            model_name='coursetest',
            name='editorial_questions',
            field=models.ManyToManyField(blank=True, to='courses.EditorialQuestion'),
        ),
        migrations.AddField(
            model_name='coursetest',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.instructor'),
        ),
        migrations.AddField(
            model_name='coursetest',
            name='multiple_choice_questions',
            field=models.ManyToManyField(blank=True, to='courses.MultipleChoiceQuestion'),
        ),
        migrations.AddField(
            model_name='coursetest',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='extras.parentcategory'),
        ),
        migrations.AddField(
            model_name='coursetest',
            name='requirements',
            field=models.ManyToManyField(blank=True, to='courses.CourseRequirement'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_category',
            field=models.ManyToManyField(blank=True, to='extras.Category'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_coupons',
            field=models.ManyToManyField(blank=True, related_name='course_coupons', to='courses.Coupon'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.instructor'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_learning_goals',
            field=models.ManyToManyField(blank=True, to='courses.CourseLearningGoal'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_parent_category',
            field=models.ManyToManyField(blank=True, to='extras.ParentCategory'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_requirements',
            field=models.ManyToManyField(blank=True, to='courses.CourseRequirement'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_sections',
            field=models.ManyToManyField(blank=True, related_name='course_sections', to='courses.Section'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_tests', to='courses.coursetest'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='extras.topic'),
        ),
        migrations.AddField(
            model_name='coupon',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_coupon', to='courses.course'),
        ),
    ]
