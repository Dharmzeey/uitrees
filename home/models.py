from django.db import models


class Search(models.Model):
    name = models.CharField(max_length=25)
    search_by = models.CharField(max_length=25)
    
    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

