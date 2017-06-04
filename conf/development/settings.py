# -*- coding: utf-8 -*-

"""
     _____  _   _   ____  _  __
    |  ___|| | | | / ___|| |/ /
    | |_   | | | || |    | ' /
    |  _|  | |_| || |___ | . \
    |_|     \___/  \____||_|\_\

     _____ __     __ _____  ____ __   __ ____    ___   ____ __   __
    | ____|\ \   / /| ____||  _ \\ \ / /| __ )  / _ \ |  _ \\ \ / /
    |  _|   \ \ / / |  _|  | |_) |\ V / |  _ \ | | | || | | |\ V /
    | |___   \ V /  | |___ |  _ <  | |  | |_) || |_| || |_| | | |
    |_____|   \_/   |_____||_| \_\ |_|  |____/  \___/ |____/  |_|


    (c) Copyright BreakWire Lab 2017 All Rights Reserved
    ---------------------------------------------------------------------------
    File Name    : settings.py
    Description  : development settings.py
    Author       : Chen Jian
    Gmail        : lsdvincent@gmail.com
    GitHub       : http://github.com/lsdlab/dangann
  -----------------------------------------------------------------------------
"""


"""
Django settings for dangann project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'flat_responsive',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user',
    'coffice',
    'articles',
    'captcha',
    'imagekit',
    'rest_framework',
    'django_extensions',
    'debug_toolbar',
    'django_rq',
    'django_celery_beat',
    'django_celery_results',
]


REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated',
    # ),
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework.authentication.SessionAuthentication',
    #     'rest_framework.authentication.BasicAuthentication',
    #     'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    # ),
    'PAGE_SIZE': 200,
    'DATETIME_FORMAT': "%Y-%m-%d",
}

JWT_AUTH = {
    'JWT_VERIFY_EXPIRATION': False
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]
INTERNAL_IPS = ('127.0.0.1')
DEBUG_TOOLBAR_CONFIG = {  'JQUERY_URL' : r"http://code.jquery.com/jquery-2.1.1.min.js"}


ROOT_URLCONF = 'dangann.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dangann.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("DATABASE_NAME"),
        'USER': os.environ.get("DATABASE_USER"),
        'PASSWORD':os.environ.get("DATABASE_PASSWORD")
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_ROOT = 'media/'
MEDIA_URL = '/media/'

AUTH_USER_MODEL = 'user.User'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'


# # celery settings
# BROKER_URL =os.environ.get("REDIS_URL")
# # redis result backend
# CELERY_RESULT_BACKEND = os.environ.get("REDIS_URL")
# # database result backend, use django-celery-results
# # CELERY_RESULT_BACKEND = 'django-db'
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TIMEZONE = 'Asia/Shanghai'

# django-rq settings
RQ_QUEUES = {
    'default': {
        'URL': os.environ.get("REDIS_URL"),
        'DEFAULT_TIMEOUT': 300,
    },
    'high': {
        'URL': os.environ.get("REDIS_URL"),
        'DEFAULT_TIMEOUT': 300,
    },
    'low': {
        'URL': os.environ.get("REDIS_URL"),
        'DEFAULT_TIMEOUT': 300,
    }
}

# django-redis settings
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.environ.get("REDIS_URL"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

REDIS_TIMEOUT = 24 * 60 * 60
