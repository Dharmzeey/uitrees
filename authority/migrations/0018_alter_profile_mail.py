# Generated by Django 4.0.1 on 2022-05-15 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authority', '0017_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mail',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]
