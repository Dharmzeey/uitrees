# Generated by Django 3.2.6 on 2022-01-09 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0010_auto_20220102_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tree',
            name='pharmacological_details',
            field=models.TextField(blank=True, null=True),
        ),
    ]