from django.db import models

# Create your models here.


class Search(models.Model):
    name = models.CharField(max_length=25)
    search_by = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Steal(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name
