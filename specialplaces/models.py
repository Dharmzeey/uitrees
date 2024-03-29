from django.db import models
from django.core.validators import MinValueValidator
from django_resized import ResizedImageField

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
    tree_picture = ResizedImageField(size=[800, None], upload_to='images/specials/%Y/%m/%d/')
    tree_picture2 =ResizedImageField(size=[500, None], upload_to='images/specials/%Y/%m/%d/', null=True, blank=True)
    tree_picture3 = ResizedImageField(size=[400, None], upload_to='images/specials/%Y/%m/%d/', null=True, blank=True)

    # I COMMENTED THIS OUT COZ I ALREADY IT WITH DJANGO_RESIZED
    # def save(self, *args, **kwargs):
    #     if 'specials/' not in self.tree_picture.url:
    #         new_image = compress(self.tree_picture)
    #         self.tree_picture = new_image
    #         new_image2 = compress(self.tree_picture2)
    #         self.tree_picture2 = new_image2
    #         new_image3 = compress(self.tree_picture3)
    #         self.tree_picture3 = new_image3
    #     super().save(*args, **kwargs)

    special_place_name = models.CharField(max_length=100, null=True, blank=True)
    location_name = models.CharField(max_length=80)
    location_description = models.TextField()
    coordinates = models.CharField(max_length=30)
    latitude = models.CharField(max_length=30)
    longitude = models.CharField(max_length=30)
    time_now = models.DateTimeField(auto_now=True)
    uploader = models.CharField(max_length=50, null=True, blank=True)

    # class Meta:
    #     ordering = ['tree_name']

    def __str__(self):
        ret_val = self.special_place_name + ' at ' + self.location_name
        return ret_val
