from .base import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = False

ALLOWED_HOSTS = ["localhost"]

# THIS IS THE ONLY SITE THAT WILL ALLOW CSRF ACCESS
# I CREATED IT MYSELF
CSRF_TRUSTED_ORIGINS = ["https://127.0.0.1"]

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'uitrees',
        'USER': 'postgres',
        'PASSWORD': 'Azeezat1@',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}
