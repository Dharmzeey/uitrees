from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator

User = settings.AUTH_USER_MODEL


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
  picture = models.ImageField(default="icons/avatar.png", upload_to="images/contributors")
  name = models.CharField(max_length=70, null=True, blank=True)
  about = models.TextField(null=True, blank=True)
  mail = models.EmailField(null=True, blank=True, unique=True)
  phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Number Must be in +234 format")
  tel = models.CharField(validators=[phone_regex], max_length=17, null=True, blank=True)
  website = models.URLField(max_length=200, null=True, blank=True)
  git_link = models.URLField(max_length=200, null=True, blank=True)
  tw_link = models.URLField(max_length=200, null=True, blank=True)
  ig_link = models.URLField(max_length=200, null=True, blank=True)
  fb_link = models.URLField(max_length=200, null=True, blank=True)

  def __str__(self):
    return str(self.user)
