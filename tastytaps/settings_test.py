from .settings import *  # noqa


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/test.db',
    }
}

DEBUG = True
TEMPLATE_DEBUG = DEBUG
