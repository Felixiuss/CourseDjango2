import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # путь к нашему проекту

SECRET_KEY = '!+ge2n97yt(=*!)-ev&beu_mzt&+f728e&1=(w#!wu)&=pv5h)'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_DIR = os.path.join(BASE_DIR, 'static')  # директория где лежит наша папка со статикой
STATICFILES_DIRS = [STATIC_DIR, ]