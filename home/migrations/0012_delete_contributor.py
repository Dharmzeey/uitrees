# Generated by Django 4.0.1 on 2022-05-07 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_contributor_delete_contributors'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contributor',
        ),
    ]