from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


#настройки для postgresql

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql', 
#         'NAME': 'db_name',
#         'USER': 'username',
#         'PASSWORD': 'password!',
#         'HOST': 'adress.yandex.ru', 
#         'PORT': '3306',
#         'ssl-mode': 'DISABLED',
#     }
# }