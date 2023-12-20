# Generated by Django 3.2.23 on 2023-12-20 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_teacheractivities_student_interaction_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoachTeacherInteraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_meeting_date', models.DateTimeField()),
                ('meeting_notes', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.coach')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.teacher')),
            ],
        ),
    ]
