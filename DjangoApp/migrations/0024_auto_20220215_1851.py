# Generated by Django 3.1.7 on 2022-02-15 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0023_leavereport_leave_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leavereport',
            name='leave_feedback',
        ),
        migrations.AddField(
            model_name='leavereport',
            name='leave_reply',
            field=models.TextField(default='null'),
        ),
    ]