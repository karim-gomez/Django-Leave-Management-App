# Generated by Django 3.1.7 on 2022-02-08 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0010_auto_20220208_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavereport',
            name='leave_feedback',
            field=models.TextField(max_length=255),
        ),
    ]
