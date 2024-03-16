# Generated by Django 5.0.1 on 2024-02-03 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorapp', '0006_alter_class_end_datetime_alter_class_schedule_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='mentorprofile',
            name='experience',
            field=models.TextField(default='', max_length=200, null=True),
        ),
    ]