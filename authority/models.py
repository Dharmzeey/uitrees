from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class MyUserCreationModel(AbstractUser):
  picture = models.ImageField(default="icons/avatar.png", upload_to="images/contributors")
  name = models.CharField(max_length=70)
  profile = models.TextField()
  mail = models.EmailField()
  phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Number Must be in +234 format")
  tel = models.CharField(validators=[phone_regex], max_length=17)
  website = models.URLField(max_length=200, null=True, blank=True)
  git_link = models.URLField(max_length=200, null=True, blank=True)
  tw_link = models.URLField(max_length=200, null=True, blank=True)
  ig_link = models.URLField(max_length=200, null=True, blank=True)
  fb_link = models.URLField(max_length=200, null=True, blank=True)


