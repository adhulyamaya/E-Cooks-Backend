# Generated by Django 5.0.1 on 2024-02-04 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorapp', '0007_class_enabled_alter_mentorprofile_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentorprofile',
            name='availability_end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mentorprofile',
            name='availability_start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
