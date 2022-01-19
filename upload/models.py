from django.db import models
from django.core.validators import MinValueValidator

from trees.models import Tree

# Create your models here.


class Upload(models.Model):
    tree_name = models.ForeignKey(Tree, on_delete=models.SET_NULL, null=True)
    tree_count = models.IntegerField(
        default=0,
        validators=[MinValueValidator(1)]
    )
    tree_picture = models.ImageField()
    tree_picture2 = models.ImageField(null=True, blank=True)
    tree_picture3 = models.ImageField(null=True, blank=True)
    location_name = models.CharField(max_length=80)
    location_description = models.TextField()
    coordinates = models.CharField(max_length=30, null=True, blank=True)
    latitude = models.CharField(max_length=30, null=True, blank=True)
    longitude = models.CharField(max_length=30, null=True, blank=True)
    time_now = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['tree_name']

    def __str__(self):
        ret_val = self.tree_name.scientific_name + ' at ' + self.location_name
        return ret_val


