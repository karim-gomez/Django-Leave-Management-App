# Generated by Django 3.1.7 on 2022-02-08 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0009_auto_20220208_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavereport',
            name='leave_feedback',
            field=models.TextField(default='this was empty'),
        ),
    ]
