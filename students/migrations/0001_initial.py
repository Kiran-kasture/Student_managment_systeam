# Generated by Django 4.0.5 on 2022-08-26 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.IntegerField(unique=True)),
                ('course', models.CharField(max_length=200)),
                ('course_timing', models.CharField(max_length=200)),
            ],
        ),
    ]
