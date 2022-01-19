# Generated by Django 4.0.1 on 2022-01-16 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0031_timeupdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timeupdate',
            old_name='time_now',
            new_name='time_then',
        ),
        migrations.AddField(
            model_name='timeupdate',
            name='name',
            field=models.CharField(default='Time', max_length=7),
        ),
        migrations.AddField(
            model_name='upload',
            name='time_now',
            field=models.DateTimeField(auto_now=True),
        ),
    ]