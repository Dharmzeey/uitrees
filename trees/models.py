from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Class(models.Model):
    tree_class = models.CharField(max_length=50)

    def __str__(self):
        return self.tree_class


class Order(models.Model):
    tree_order = models.CharField(max_length=50)

    def __str__(self):
        return self.tree_order


class Family(models.Model):
    tree_family = models.CharField(max_length=50)

    def __str__(self):
        return self.tree_family


class ConservationStatus(models.Model):
    tree_status = models.CharField(max_length=50)

    def __str__(self):
        return self.tree_status


class SpecieStatus(models.Model):
    specie_status = models.CharField(max_length=20)

    def __str__(self):
        return self.specie_status


class Tree(models.Model):
    scientific_name = models.CharField(
        max_length=100,
        help_text='Enter Generic, Specific and Author',
        validators=[MinLengthValidator(3, 'Must be greater than 3')],
        null=False
    )
    authority = models.CharField(max_length=80, default='------')
    common_name = models.CharField(max_length=50, default='------')
    local_name = models.CharField(max_length=50, default='------')

    conservation_status = models.ForeignKey(ConservationStatus, on_delete=models.SET_NULL, null=True)
    specie_status = models.ForeignKey(SpecieStatus, on_delete=models.SET_NULL, null=True)
    # CLASS IS VERY COMPLICATED TO ADD
    # tree_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
    tree_order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    tree_family = models.ForeignKey(Family, on_delete=models.SET_NULL, null=True)
    tree_description = models.TextField()
    pharmacological_details = models.TextField(default=' ')
    last_updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['scientific_name']

    def __str__(self):
        return self.scientific_name
