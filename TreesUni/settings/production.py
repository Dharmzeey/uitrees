from .base import *

DEBUG = True

ALLOWED_HOSTS = ['uitrees.herokuapp.com']

# THIS IS THE ONLY SITE THAT WILL ALLOW CSRF ACCESS
# I CREATED IT MYSELF
CSRF_TRUSTED_ORIGINS = ["https://uitrees.herokuapp.com"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'uitrees',
    #     'USER': 'postgres',
    #     'PASSWORD': 'Azeezat1@',
    #     'HOST': '127.0.0.1',
    #     'PORT': '',
    # }
}

# db_from_env = dj_database_url.config(conn_max_age=600)
# DATABASES['default'].update(db_from_env)