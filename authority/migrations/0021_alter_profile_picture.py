# Generated by Django 4.0.4 on 2022-12-11 07:06

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('authority', '0020_rename_user_profile_owner_alter_profile_mail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=django_resized.forms.ResizedImageField(crop=None, default='icons/avatar.png', force_format=None, keep_meta=True, quality=-1, scale=None, size=[200, 200], upload_to='images/contributors'),
        ),
    ]
