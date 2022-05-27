from pathlib import Path
import os
from environ import Env

env = Env()
Env().read_env()

BASE_DIR = Path(__file__).resolve().parent.parent


SQL_LITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

POSTGRES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'taskdb',
        'USER': os.environ['PSQL_USER'],
        'PASSWORD': os.environ['PSQL_PASSWORD'],
        'HOST': 'localhost',
        'PORT': '5432',
    }
}