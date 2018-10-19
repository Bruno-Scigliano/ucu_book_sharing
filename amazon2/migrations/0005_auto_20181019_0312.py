# Generated by Django 2.1.2 on 2018-10-19 03:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon2', '0004_notification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='time_sent',
        ),
        migrations.AddField(
            model_name='notification',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='notification',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Seen', 'Seen')], default='New', max_length=15),
        ),
    ]