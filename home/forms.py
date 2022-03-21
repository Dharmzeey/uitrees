from django.forms import ModelForm
from .models import Contributor
from django.contrib.auth.models import User


class ProfileFrom(ModelForm):
    class Meta:
        model = Contributor
        fields = '__all__'
        exclude = ('user',)


# class UserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'
