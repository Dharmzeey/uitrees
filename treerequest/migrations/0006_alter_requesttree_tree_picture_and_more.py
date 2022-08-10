# Generated by Django 4.0.1 on 2022-05-07 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treerequest', '0005_alter_requesttree_tree_picture2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requesttree',
            name='tree_picture',
            field=models.ImageField(upload_to='images/request/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='requesttree',
            name='tree_picture2',
            field=models.ImageField(blank=True, null=True, upload_to='images/request/%Y/%m/%d/'),
        ),
    ]