from .base import *
from .base import env


# GENERAL
DEBUG = False
ALLOWED_HOSTS = [env('DJANGO_ALLOWED_HOSTS')]

# ADMIN
ADMIN_URL = env('DJANGO_ADMIN_URL')

# DATABASES
DATABASES = {
    'default': {
         'ENGINE': env('DB_ENGINE'),
         'NAME': env('DB_NAME'),
         'USER': env('DB_USER'),
         'PASSWORD': env('DB_PASSWORD'),
         'HOST': env('DB_HOST'),
         'PORT': env('DB_PORT'),
         'OPTIONS': {
            'options': '-c search_path=' + env('DB_SCHEMA'),
         },
         'ATOMIC_REQUESTS': True,
     }
}
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# SECURITY

# STORAGES

# STATIC & MEDIA
STATIC_URL = ''
MEDIA_URL = ''

# PASSWORDS
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS':{"min_length":8}
    },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# SESSION
SESSION_COOKIE_AGE = 3600 * 24
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# EMAIL

# LOGGING
