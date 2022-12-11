from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django_resized import ResizedImageField

User = settings.AUTH_USER_MODEL


class Profile(models.Model):
  owner = models.OneToOneField(User, on_delete=models.CASCADE)
  picture = ResizedImageField(size=[200, 200], default="icons/avatar.png", upload_to="images/contributors")
  name = models.CharField(max_length=70, null=True)
  about = models.TextField(null=True, blank=True)
  mail = models.EmailField(null=True, unique=True)
  phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Number Must be in +234 format")
  tel = models.CharField(validators=[phone_regex], max_length=17, null=True, blank=True)
  website = models.URLField(max_length=200, null=True, blank=True)
  git_link = models.URLField(max_length=200, null=True, blank=True)
  tw_link = models.URLField(max_length=200, null=True, blank=True)
  ig_link = models.URLField(max_length=200, null=True, blank=True)
  fb_link = models.URLField(max_length=200, null=True, blank=True)

  def __str__(self):
    return str(self.owner)
  
  class Meta:
    ordering = ["owner"]
