# Generated by Django 4.0.1 on 2022-03-19 19:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0010_contributors_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='contributors/%Y/%m/%d/')),
                ('name', models.CharField(max_length=70)),
                ('profile', models.TextField()),
                ('mail', models.EmailField(max_length=254)),
                ('tel', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message='Number Must be in +234 format', regex='^\\+?1?\\d{9,15}$')])),
                ('website', models.URLField(blank=True, null=True)),
                ('git_link', models.URLField(blank=True, null=True)),
                ('tw_link', models.URLField(blank=True, null=True)),
                ('ig_link', models.URLField(blank=True, null=True)),
                ('fb_link', models.URLField(blank=True, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Contributors',
        ),
    ]
