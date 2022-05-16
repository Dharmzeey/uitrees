# Generated by Django 4.0.4 on 2022-05-15 17:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authority', '0015_remove_profile_profile_profile_about_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='tel',
            field=models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message='Number Must be in +234 format', regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
