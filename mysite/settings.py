"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%*03qgpl^b)gxyle&gwj0_2*nk9e0tl38lsch31uy0c_a7yitl'

# SECURITY WARNING: don't run with debug turned on in production!
if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine'):
    DEBUG = False
else:
    DEBUG = True

ALLOWED_HOSTS = ['.appspot.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pvs.apps.PvsConfig'
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

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                os.path.join(BASE_DIR,'pvcApp','app','views'),
                os.path.join(BASE_DIR,'webapp','app'),
                os.path.join(BASE_DIR,'templates')
            ],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine'):
    # Running on production App Engine, so use a Google Cloud SQL database.
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '/cloudsql/solar-cloud-143410:asia-east1:pvc-db1',
            'NAME': 'pvcloud',
            'USER': 'pvcloud',
            'PASSWORD': 'zaq12wsx',
        }
    }
else:
    import socket
    try:
        HOSTNAME = socket.gethostname()
    except:
        HOSTNAME = 'localhost'
    
    if HOSTNAME == 'pvcloud-compute-1':
        DB_HOST = '104.199.200.37'
    else:
        DB_HOST = 'localhost'
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'pvcloud',
            'USER': 'pvcloud',
            'PASSWORD': 'zaq12wsx',
            'HOST': DB_HOST,
            'PORT': '3306',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static/')

STATICFILES_DIRS = [
                    #os.path.join(BASE_DIR,"static"),
                    ("doc", os.path.join(BASE_DIR,"doc","_build","html")),
                    ("fonts", os.path.join(BASE_DIR,"webapp","app","fonts")),
                    ("js", os.path.join(BASE_DIR,"webapp","app","js")),
                    ("css", os.path.join(BASE_DIR,"webapp","app","css")),
                    ("amcharts", os.path.join(BASE_DIR,"webapp","bower_components","amcharts","dist","amcharts")),
                    ("bower_components", os.path.join(BASE_DIR,"pvcApp","bower_components")),
                    ("styles", os.path.join(BASE_DIR,"pvcApp","app","styles")),
                    ("scripts", os.path.join(BASE_DIR,"pvcApp","app","scripts")),
                    ("images", os.path.join(BASE_DIR,"pvcApp","app","images")),
                    #("styles", os.path.join(BASE_DIR,"webapp","dist","styles")),
                    #("scripts", os.path.join(BASE_DIR,"webapp","dist","scripts")),
                    #("fonts", os.path.join(BASE_DIR,"webapp","dist","fonts")),
                    ]

LOGGING = {
    'version': 1,              
    'disable_existing_loggers': False,  # this fixes the problem

    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "standard",
            "stream": "ext://sys.stdout"
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG'
    },
    'loggers': {
        'pvs': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False
        },
        'pvs.views_admin': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'pvs.views_user': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}
