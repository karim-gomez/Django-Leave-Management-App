# Generated by Django 3.1.7 on 2022-01-10 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0002_auto_20211231_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]