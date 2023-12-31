# Generated by Django 3.2.23 on 2023-12-20 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_resourcemanagement'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherActivities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_active', models.DateTimeField()),
                ('activity_score', models.IntegerField(default=0)),
                ('student_interaction_rating', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.teacher')),
            ],
        ),
    ]
