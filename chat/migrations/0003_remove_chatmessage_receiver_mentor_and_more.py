# Generated by Django 5.0.1 on 2024-03-24 09:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_remove_chatmessage_receiver_and_more'),
        ('mentorapp', '0017_alter_class_thumbnail'),
        ('myapp', '0007_userprofile_blocked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatmessage',
            name='receiver_mentor',
        ),
        migrations.RemoveField(
            model_name='chatmessage',
            name='receiver_user',
        ),
        migrations.RemoveField(
            model_name='chatmessage',
            name='sender_mentor',
        ),
        migrations.RemoveField(
            model_name='chatmessage',
            name='sender_user',
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='receiver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to='mentorapp.mentorprofile'),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='receiver_type',
            field=models.CharField(choices=[('user', 'User'), ('mentor', 'Mentor')], default='user', max_length=10),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to='myapp.userprofile'),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='sender_type',
            field=models.CharField(choices=[('user', 'User'), ('mentor', 'Mentor')], default='user', max_length=10),
        ),
    ]
