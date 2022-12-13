# Generated by Django 4.1.4 on 2022-12-13 22:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("upload", "0046_alter_upload_temp_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="upload",
            name="id",
        ),
        migrations.AlterField(
            model_name="upload",
            name="temp_id",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
