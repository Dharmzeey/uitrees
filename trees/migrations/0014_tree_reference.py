# Generated by Django 4.0.1 on 2022-01-26 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0013_alter_tree_genus_specie'),
    ]

    operations = [
        migrations.AddField(
            model_name='tree',
            name='reference',
            field=models.URLField(default='https://powo.science.kew.org'),
        ),
    ]
