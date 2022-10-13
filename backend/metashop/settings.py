"""
Django 4.1.2.
"""

from split_settings.tools import include
from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()

include(
    'components/auth_password_validators.py',
    'components/installed_apps.py',
    'components/middleware.py',
    'components/templates.py',
    'components/databases.py',
) 

DEBUG = True
ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = ["*"]


#SECRET_KEY = os.environ.get('SECRET_KEY', default=None),
SECRET_KEY = 'django-insecure--d59p3^1=pq%+do05-xzt1ol=q4zl*mmrdd77x*6d*tp7&20oq'
BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_URLCONF = 'metashop.urls'
WSGI_APPLICATION = 'metashop.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True


STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')



