# Generated by Django 4.0.1 on 2022-01-27 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0015_authority_alter_tree_authority'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tree',
            old_name='authority',
            new_name='tree_authority',
        ),
        migrations.AlterField(
            model_name='authority',
            name='tree_authority',
            field=models.CharField(max_length=100),
        ),
    ]