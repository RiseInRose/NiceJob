"""
Django settings for NiceJob project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xt!wmuwol2hnu#$2svpd)7#6a)b-ejpiy!%3g=hx+d$0wy_=50'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','localhost','.muguayun.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'job_web',
    'myusers',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'NiceJob.urls'

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

WSGI_APPLICATION = 'NiceJob.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nicejob',
        'USER': 'root',
        'PASSWORD': 'hb123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
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
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
AUTH_USER_MODEL = 'myusers.User'
# AUTH_USER_MODEL 是替换成自定义的用户认证

LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
# 设置登录后，注销后。跳转的页面。
LOGOUT_REDIRECT_URL = '/myusers/login/'
LOGIN_REDIRECT_URL = '/job_web/mine/?a='
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# 设置使用邮箱登录
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'myusers.backends.EmailBackend',
)

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
from mongoengine import connect
connect('NiceJob',host = '127.0.0.1',port=27017)

# from django.db import connections
# cursor = connections['cds'].cursor()

# ----------------
USERS_REGISTRATION_OPEN = True

USERS_VERIFY_EMAIL = True

USERS_AUTO_LOGIN_ON_ACTIVATION = True

USERS_EMAIL_CONFIRMATION_TIMEOUT_DAYS = 3

# Specifies minimum length for passwords:
USERS_PASSWORD_MIN_LENGTH = 5

# Specifies maximum length for passwords:
USERS_PASSWORD_MAX_LENGTH = None

# the complexity validator, checks the password strength
USERS_CHECK_PASSWORD_COMPLEXITY = True

USERS_SPAM_PROTECTION = False  # important!

#  ---------------------------------------------------------
#  Email
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_SSL = True
# EMAIL_HOST = 'smtp.163.com'
# EMAIL_PORT = 25
# #发送邮件的邮箱
# EMAIL_HOST_USER = '18571673020@163.com'
# #在邮箱中设置的客户端授权密码
# EMAIL_HOST_PASSWORD = 'Hb123456'
#
# #收件人看到的发件人
# EMAIL_FROM = 'cbd'
#  ---------------------------------------------------------