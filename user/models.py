import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from django_resized import ResizedImageField



class User(AbstractUser):
  id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True, primary_key=True)
  picture = ResizedImageField(size=[700, 700], default="icons/avatar.png", upload_to="images/contributors")
  about = models.TextField(null=True, blank=True)
  phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Number Must be in +234 format")
  email = models.EmailField(unique=True, null=False, blank=False)
  tel = models.CharField(validators=[phone_regex], max_length=17, null=True, blank=True)
  website = models.URLField(max_length=200, null=True, blank=True)
  git_link = models.URLField(max_length=200, null=True, blank=True)
  tw_link = models.URLField(max_length=200, null=True, blank=True)
  ig_link = models.URLField(max_length=200, null=True, blank=True)
  fb_link = models.URLField(max_length=200, null=True, blank=True)
  
  REQUIRED_FIELDS = ["email"]

  
  class Meta:
    ordering = ["first_name"]
