# Generated by Django 4.0.1 on 2022-02-15 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treerequest', '0002_alter_requesttree_tree_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requesttree',
            name='tree_picture',
            field=models.ImageField(upload_to='request/%Y/%m/%d'),
        ),
    ]
