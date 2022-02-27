from django.db import models
from utilities.compressor import compress


class Search(models.Model):
    name = models.CharField(max_length=25)
    search_by = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Contributors(models.Model):
    picture = models.ImageField(upload_to='contributors/%Y/%m/%d/')

    def save(self, *args, **kwargs):
        new_image = compress(self.picture)
        self.picture = new_image
        super().save(*args, **kwargs)

    name = models.CharField(max_length=50)
    profile = models.TextField()
    mail = models.EmailField()
    tel = models.IntegerField(default=234)
    website = models.URLField(max_length=200, null=True, blank=True)
    git_link = models.URLField(max_length=200, null=True, blank=True)
    tw_link = models.URLField(max_length=200, null=True, blank=True)
    ig_link = models.URLField(max_length=200, null=True, blank=True)
    fb_link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
