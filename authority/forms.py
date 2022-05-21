from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import Profile


class ProfileCreateFrom(UserCreationForm):
  class Meta:
    model = User
    fields = ("username", "email", "password1", "password2")

  # THIS BELOW ENSURES THAT WE DO NOT HAVE DUPLICATE EMAIL
  def clean_email(self):
    email = self.cleaned_data['email']
    if User.objects.filter(email=email).exists():
      raise ValidationError("Email ALready Exists")
    return email


class ProfileUpdateForm(ModelForm):
  class Meta:
    model = Profile
    fields = "__all__"
    exclude = ('owner',)

