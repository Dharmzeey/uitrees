# Generated by Django 3.2.6 on 2022-01-09 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0023_alter_upload_coordinates'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='latitude',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='upload',
            name='longitude',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
