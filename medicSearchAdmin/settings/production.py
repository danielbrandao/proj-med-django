import os

from .settings import *

DEBUG = True

# Cria a secretkey de ambiente teste
SECRET_KEY = '1234qwerasdf'

# Config IP do ambiente que irá executar
ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}