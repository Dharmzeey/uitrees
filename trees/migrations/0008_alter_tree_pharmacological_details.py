# Generated by Django 3.2.6 on 2022-01-02 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0007_auto_20220102_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tree',
            name='pharmacological_details',
            field=models.TextField(default=' '),
        ),
    ]
