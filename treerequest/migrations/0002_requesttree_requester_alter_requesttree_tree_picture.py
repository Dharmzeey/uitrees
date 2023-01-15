# Generated by Django 4.1.4 on 2023-01-13 22:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("treerequest", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="requesttree",
            name="requester",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="requester",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="requesttree",
            name="tree_picture",
            field=django_resized.forms.ResizedImageField(
                crop=None,
                force_format=None,
                keep_meta=True,
                quality=-1,
                scale=None,
                size=[700, None],
                upload_to="images/request/%Y/%m/%d",
            ),
        ),
        migrations.AddField(
            model_name="requesttree",
            name="validated",
            field=models.BooleanField(default=False),
        ),
    ]