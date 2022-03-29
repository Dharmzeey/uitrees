# Generated by Django 4.0.1 on 2022-03-07 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0036_alter_upload_tree_picture_alter_upload_tree_picture2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TreeStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='upload',
            name='health_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='upload.treestatus'),
        ),
    ]