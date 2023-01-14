import uuid
from django.db import models
from django.core.validators import MinValueValidator
from django_resized import ResizedImageField
from django.conf import settings

from trees.models import Tree
# THIS BELOW IS A PACKAGE THAT CONTAINS A FUNCTION THAT
# I MANUALLY CREATE TO COMPRESS Images
from utilities.compressor import compress

User = settings.AUTH_USER_MODEL

class TreeStatus(models.Model):
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.status


class Upload(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True, primary_key=True)
    tree_name = models.ForeignKey(Tree, on_delete=models.SET_NULL, null=True)
    tree_count = models.IntegerField(
        default=0,
        validators=[MinValueValidator(1)]
    )
    tree_picture = ResizedImageField(size=[800, None], upload_to='images/uploads/%Y/%m/%d/')
    tree_picture2 = ResizedImageField(size=[500, None], upload_to='images/uploads/%Y/%m/%d/', null=True, blank=True)
    tree_picture3 = ResizedImageField(size=[500, None], upload_to='images/uploads/%Y/%m/%d/', null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     if 'uploads/' not in self.tree_picture.url:
    #         new_image = compress(self.tree_picture)
    #         self.tree_picture = new_image
    #         new_image2 = compress(self.tree_picture2)
    #         self.tree_picture2 = new_image2
    #         new_image3 = compress(self.tree_picture3)
    #         self.tree_picture3 = new_image3
    #     super().save(*args, **kwargs)
    health_status = models.ForeignKey(TreeStatus, on_delete=models.SET_NULL, null=True)

    location_name = models.CharField(max_length=80)
    location_description = models.TextField()
    coordinates = models.CharField(max_length=30, null=True, blank=True)
    latitude = models.CharField(max_length=30, null=True, blank=True)
    longitude = models.CharField(max_length=30, null=True, blank=True)
    time_now = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="uploaded_by")
    requested_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="requested_by")

    class Meta:
        ordering = ['location_name']

    def __str__(self):
        ret_val = self.tree_name.scientific_name + ' at ' + self.location_name
        return ret_val


