from .base import *

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False

ALLOWED_HOSTS = ['uitrees.up.railway.app', "uitrees.olanrewajuadam.com.ng"]

# THIS IS THE ONLY SITE THAT WILL ALLOW CSRF ACCESS
# I CREATED IT MYSELF
CSRF_TRUSTED_ORIGINS = ["https://uitrees.up.railway.app", "https://uitrees.olanrewajuadam.com.ng"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('PGDATABASE'),
        'USER':os.environ.get('PGUSER'),
        'PASSWORD':os.environ.get('PGPASSWORD'),
        'HOST':os.environ.get('PGHOST'),
        'PORT':os.environ.get('PGPORT')

}
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'olanrewa_uitrees',
#         'USER':'olanrewa_uitrees',
#         'PASSWORD':']kvm=iY+mS0i',
#         'HOST':'localhost',
#         'PORT': 3306

# }
# }

# MEDIA_ROOT = '/home/olanrewa/uitrees_media/files/media'
# STATIC_ROOT = '/home/olanrewa/uitrees_media/files/static'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
MEDIA_ROOT = '/home/olanrewa/uitrees_root/media'
# STATIC_ROOT = '/home/olanrewa/uitrees_root/static'
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT=os.path.join(BASE_DIR,'assets')



# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME': os.environ.get('CLOUD_NAME'),
#     'API_KEY': os.environ.get('API_KEY'),
#     'API_SECRET': os.environ.get('API_SECRET'),
# }
# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'