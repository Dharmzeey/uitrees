# Generated by Django 4.0.1 on 2022-05-07 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authority', '0009_alter_myusercreationmodel_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myusercreationmodel',
            name='picture',
            field=models.ImageField(default='icons/avatar.png', upload_to=''),
        ),
    ]
