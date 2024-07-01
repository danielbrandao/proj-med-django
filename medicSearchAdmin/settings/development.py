import os.path

from .settings import *

DEBUG = True

# cria a secret key para ambiente dev
SECRET_KEY = '1234qwerasdf'

# Config IP do ambiente que irá executar
ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    # Para SQLITE
    # 'default':{
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    # }

    # Para PGSQL
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db-livro-django',
        'USER': 'postgres',
        'PASSWORD': '654321',
        'HOST': 'localhost',
        'PORT': 5432
    }
}