# Generated by Django 4.0.1 on 2022-02-12 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_contributors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contributors',
            name='mail',
        ),
    ]
