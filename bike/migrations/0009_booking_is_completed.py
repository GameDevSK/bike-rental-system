# Generated by Django 3.1.5 on 2021-02-19 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0008_auto_20210219_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
