from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import Profile


class ProfileCreateFrom(UserCreationForm):
  class Meta:
    model = User
    fields = ("username", "password1", "password2")
  #
  # def save(self, commit=True):
  #   user = super(ProfileCreateFrom, self).save(commit=False)
  #   user.email = self.cleaned_data['email']
  #   if commit:
  #     user.save()
  #   return user


class ProfileUpdateForm(ModelForm):
  class Meta:
    model = Profile
    fields = "__all__"
    exclude = ('user',)

