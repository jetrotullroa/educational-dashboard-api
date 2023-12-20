# Generated by Django 3.2.23 on 2023-12-20 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20231219_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('utilization_rate', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('allocated_teachers', models.ManyToManyField(to='base.Teacher')),
            ],
        ),
    ]
