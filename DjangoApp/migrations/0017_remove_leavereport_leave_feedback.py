# Generated by Django 3.1.7 on 2022-02-08 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0016_leavereport_leave_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leavereport',
            name='leave_feedback',
        ),
    ]