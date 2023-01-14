from .base import *

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False

ALLOWED_HOSTS = ['uitrees.up.railway.app']

# THIS IS THE ONLY SITE THAT WILL ALLOW CSRF ACCESS
# I CREATED IT MYSELF
CSRF_TRUSTED_ORIGINS = ["https://uitrees.up.railway.app"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('PGDATABASE'),
        'USER':os.environ.get('PGUSER'),
        'PASSWORD':os.environ.get('PGPASSWORD'),
        'HOST':os.environ.get('PGHOST'),
        'PORT':os.environ.get('PGPORT')

}
}


CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUD_NAME'),
    'API_KEY': os.environ.get('API_KEY'),
    'API_SECRET': os.environ.get('API_SECRET'),
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'