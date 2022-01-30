# Generated by Django 4.0.1 on 2022-01-27 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0017_rename_tree_authority_tree_authority'),
    ]

    operations = [
        migrations.AddField(
            model_name='tree',
            name='tree_authority',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trees.authority'),
        ),
        migrations.AlterField(
            model_name='tree',
            name='authority',
            field=models.CharField(default='------', max_length=50),
        ),
    ]
