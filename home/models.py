from django.db import models
from utilities.compressor import compress
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class Search(models.Model):
    name = models.CharField(max_length=25)
    search_by = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Contributor(models.Model):
    picture = models.ImageField(upload_to='contributors/%Y/%m/%d/')

    def save(self, *args, **kwargs):
        if 'contributors/' not in self.picture.url:
            new_image = compress(self.picture)
            self.picture = new_image
        super().save(*args, **kwargs)

    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=70)
    profile = models.TextField()
    mail = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Number Must be in +234 format")
    tel = models.CharField(validators=[phone_regex], max_length=17)
    website = models.URLField(max_length=200, null=True, blank=True)
    git_link = models.URLField(max_length=200, null=True, blank=True)
    tw_link = models.URLField(max_length=200, null=True, blank=True)
    ig_link = models.URLField(max_length=200, null=True, blank=True)
    fb_link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
