# Generated by Django 3.2.6 on 2022-01-04 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0009_alter_upload_tree_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='tree_picture',
            field=models.ImageField(upload_to=''),
        ),
    ]
