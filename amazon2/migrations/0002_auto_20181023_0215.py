# Generated by Django 2.1.2 on 2018-10-23 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon2', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='name',
            new_name='id',
        ),
        migrations.AddField(
            model_name='genre',
            name='display_name',
            field=models.CharField(default='d', max_length=60),
            preserve_default=False,
        ),
    ]
