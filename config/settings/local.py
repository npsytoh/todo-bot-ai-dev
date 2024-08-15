from .base import *
from .base import env


# GENERAL
DEBUG = True
ALLOWED_HOSTS = ['localhost', '*']

# ADMIN
ADMIN_URL = "admin/"

# DATABASES
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'ATOMIC_REQUESTS': True,
    }
}
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# PASSWORDS
AUTH_PASSWORD_VALIDATORS = []

# STATIC & MEDIA
STATIC_URL = '/static/'
STATICFILES_DIRS = [ BASE_DIR / 'static' ]
MEDIA_URL = '/media/'
MEDIA_ROOT = [ BASE_DIR / 'media' ]

# EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# django-debug-toolbar
if DEBUG:
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]
    INSTALLED_APPS += [
        'debug_toolbar',
    ]
    DEBUG_TOOLBAR_CONFIG = {
            'INTERCEPT_REDIRECTS': False,
        }
    INTERNAL_IPS = ['127.0.0.1','10.0.2.2']
