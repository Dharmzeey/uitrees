# Generated by Django 4.1.4 on 2022-12-13 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("upload", "0047_remove_upload_id_alter_upload_temp_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="upload",
            old_name="temp_id",
            new_name="id",
        ),
    ]
