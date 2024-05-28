from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2n^#+mll5a-lsp!d!wze=o^kd0@)0!vn$q@ro*3deri&@t%6sf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []



# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'PORT':5432,
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'NAME': 'dbempleado',
    }   
}



STATIC_URL = 'static/'