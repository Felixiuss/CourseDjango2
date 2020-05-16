import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # путь к нашему проекту

SECRET_KEY = 'sgefsdhgr457-ev&beu_mzt&+f728e&1=(w#!wu)&=xfgdrs586df'

DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': 'user_name',
        'PASSWORD': 'pass',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackends'

DEFAULT_FROM__EMAIL = 'email'
EMAIL_HOST = 'smtp'
EMAIL_HOST_USER = 'email'
EMAIL_HOST_PASSWORD = 'pass'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
