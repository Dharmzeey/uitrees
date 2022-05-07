from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import MyUserCreationModel


class MyUserCreationFrom(UserCreationForm):
  class Meta:
    model = MyUserCreationModel
    fields = ['username', 'email', 'password1', 'password2']


class MyUserUpdateForm(ModelForm):
  class Meta:
    model = MyUserCreationModel
    fields = ["picture", "name", "profile", "mail", "tel", "website", "git_link", "tw_link", "ig_link", "fb_link"]
