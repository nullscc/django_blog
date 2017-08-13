from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_blog',
        'USER':os.environ['DGDB_USER'],
        'PASSWORD':os.environ['DGDB_PASSWD'],
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }
}  
USE_TZ = True 
SECRET_KEY = os.environ['SECRET_KEY']

