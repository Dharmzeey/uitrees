# Generated by Django 3.2.6 on 2022-01-01 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0002_auto_20220101_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tree',
            name='location_description',
        ),
        migrations.RemoveField(
            model_name='tree',
            name='location_name',
        ),
    ]
