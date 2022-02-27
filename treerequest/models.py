from django.db import models

# THIS BELOW IS A PACKAGE THAT CONTAINS A FUNCTION THAT
# I MANUALLY CREATE TO COMPRESS Images
from utilities.compressor import compress


class RequestTree(models.Model):
    location_name = models.CharField(max_length=100)
    location_description = models.TextField()
    tree_picture = models.ImageField(upload_to='request/%Y/%m/%d')
    tree_picture2 = models.ImageField(upload_to='request/%Y/%m/%d/', null=True, blank=True)

    def save(self, *args, **kwargs):
        new_image = compress(self.tree_picture)
        self.tree_picture = new_image
        new_image2 = compress(self.tree_picture2)
        self.tree_picture2 = new_image2
        super().save(*args, **kwargs)

    coordinates = models.CharField(max_length=30, null=True, blank=True)
    latitude = models.CharField(max_length=30, null=True, blank=True)
    longitude = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        ret_val = self.location_name + ' found at ' + self.location_description
        return ret_val
