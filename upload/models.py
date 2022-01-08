from django.db import models

from trees.models import Tree

# Create your models here.


class Upload(models.Model):
    tree_name = models.ForeignKey(Tree, on_delete=models.SET_NULL, null=True)
    tree_picture = models.ImageField()
    location_name = models.CharField(max_length=80)
    location_description = models.TextField()
    # coordinates =

    class Meta:
        ordering = ['tree_name']

    def __str__(self):
        ret_val = self.tree_name.scientific_name + ' at ' + self.location_name
        return ret_val
