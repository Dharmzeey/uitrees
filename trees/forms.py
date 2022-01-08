from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from . import models


class ClassCreateForm(ModelForm):
    class Meta:
        model = models.Class
        fields = '__all__'


class OrderCreateForm(ModelForm):
    class Meta:
        model = models.Order
        fields = '__all__'


class FamilyCreateForm(ModelForm):
    class Meta:
        model = models.Family
        fields = '__all__'
