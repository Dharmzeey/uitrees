# Generated by Django 4.0.4 on 2022-12-11 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authority', '0021_alter_profile_picture'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['owner']},
        ),
    ]
