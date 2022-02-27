from django.db import models
from django.core.validators import MinValueValidator

from trees.models import Tree

# THIS BELOW IS A PACKAGE THAT CONTAINS A FUNCTION THAT
# I MANUALLY CREATE TO COMPRESS Images
from utilities.compressor import compress


class SpecialPlace(models.Model):
    tree_specie_found = models.ManyToManyField(Tree)
    tree_count = models.IntegerField(
        default=0,
        validators=[MinValueValidator(1)]
    )
    tree_picture = models.ImageField(upload_to='specials/%Y/%m/%d/')
    tree_picture2 = models.ImageField(upload_to='specials/%Y/%m/%d/', null=True, blank=True)
    tree_picture3 = models.ImageField(upload_to='specials/%Y/%m/%d/', null=True, blank=True)

    def save(self, *args, **kwargs):
        new_image = compress(self.tree_picture)
        self.tree_picture = new_image
        new_image2 = compress(self.tree_picture2)
        self.tree_picture2 = new_image2
        new_image3 = compress(self.tree_picture3)
        self.tree_picture3 = new_image3
        super().save(*args, **kwargs)

    special_place_name = models.CharField(max_length=100, null=True, blank=True)
    location_name = models.CharField(max_length=80)
    location_description = models.TextField()
    coordinates = models.CharField(max_length=30, null=True, blank=True)
    latitude = models.CharField(max_length=30, null=True, blank=True)
    longitude = models.CharField(max_length=30, null=True, blank=True)
    time_now = models.DateTimeField(auto_now=True)

    # class Meta:
    #     ordering = ['tree_name']

    def __str__(self):
        ret_val = self.special_place_name + ' at ' + self.location_name
        return ret_val
