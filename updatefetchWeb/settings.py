"""
For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-z598azztc*nqh_m%q_2@9s9^rny$pvblq2v#pd=kqu7qp)8qb4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# -- begin self-defined variables --
PLATFORM_CHOICES = (
    ('windows', 'Windows'),
    ('android', 'Android'),
    ('linux', 'Linux'),
)

ARCHITECTURE_CHOICES = (
    ('amd64', 'AMD64'),
    ('arm64', 'ARM64'),
)

# 更灵活的请求最新网址
AMD64_ALIAS = {'standard_name': 'amd64', 'alias': {"amd64", "x64"}}
ARM64_ALIAS = {'standard_name': 'arm64', 'alias': {"arm64", "arm"}}
Windows_ALIAS = {'standard_name': 'windows', 'alias': {"windows", "win"}}
Android_ALIAS = {'standard_name': 'android', 'alias': {"android", "ad"}}
Linux_ALIAS = {'standard_name': 'linux', 'alias': {"linux"}}

# 生成一些下面程序需要的数据
SYSTEM_LIST = [Windows_ALIAS, Android_ALIAS, Linux_ALIAS]
ARCH_LIST = [AMD64_ALIAS, ARM64_ALIAS]
ALL_SYSTEM = Windows_ALIAS['alias'] | Android_ALIAS['alias'] | Linux_ALIAS['alias']
ALL_ARCH = AMD64_ALIAS['alias'] | ARM64_ALIAS['alias']
ALL_SYSTEM_ARCH = ALL_ARCH | ALL_SYSTEM


REST_FRAMEWORK = {
   'DEFAULT_AUTHENTICATION_CLASSES': [
	   'rest_framework.authentication.TokenAuthentication',
       'rest_framework.authentication.SessionAuthentication',
	   # 可供选择的验证的方式...
   ],
   'DEFAULT_PERMISSION_CLASSES': [
	   'rest_framework.permissions.IsAuthenticated',
	   # 要求必须经过了验证才能使用...
   ],
}

# -- end self-defined variables --


# Application definition

INSTALLED_APPS = [
    'homepage.apps.HomepageConfig',
    'upload.apps.UploadConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken'
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

ROOT_URLCONF = 'updatefetchWeb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'updatefetchWeb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = '/home/hoo/static/updatefetch'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


try:
    from .local_settings import *
except ImportError:
    pass
