# Generated by Django 4.0.4 on 2022-05-15 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authority', '0014_profile_delete_myusercreationmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile',
        ),
        migrations.AddField(
            model_name='profile',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]