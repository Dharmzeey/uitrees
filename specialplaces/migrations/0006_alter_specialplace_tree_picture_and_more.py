# Generated by Django 4.0.1 on 2022-02-12 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialplaces', '0005_alter_specialplace_tree_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialplace',
            name='tree_picture',
            field=models.ImageField(upload_to='images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='specialplace',
            name='tree_picture2',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='specialplace',
            name='tree_picture3',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d/'),
        ),
    ]
