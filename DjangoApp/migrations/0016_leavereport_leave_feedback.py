# Generated by Django 3.1.7 on 2022-02-08 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0015_remove_leavereport_leave_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='leavereport',
            name='leave_feedback',
            field=models.TextField(null=True),
        ),
    ]