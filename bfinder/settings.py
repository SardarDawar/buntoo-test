import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'users/static'),
    os.path.join(BASE_DIR, 'trading/static'),
    os.path.join(BASE_DIR, 'chat/static')

)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jmwxa26jd#cju^%x+8ydw*1po$-bpb@y5y^qwy46gj&6_1*du%'

# FOREX_LOGIN_AND_PASS =
# brookrodia@gmail.com
# BRookrodia

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['blockfinder.herokuapp.com',
                 'blockfinderinc.com', 'www.blockfinderinc.com', '127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    # added trading config from apps.py so Django recognizes app templates and models
    'trading.apps.TradingConfig',
    'users.apps.UsersConfig',
    'crispy_forms',  # makes it easier to style forms
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'chat',
    'ckeditor',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth.registration',


]

SITE_ID = 1
from rest_framework import compat
compat.md_filter_add_syntax_highlight = lambda md: False
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'chat.middleware.ActiveUserMiddleware',

]

ROOT_URLCONF = 'bfinder.urls'

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

                # friends list 
                'trading.context_preprocessors.friends',
            ],
        },
    },
]

WSGI_APPLICATION = 'bfinder.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# tell Crispy forms which version of Bootsrap to use
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# The Redirect View the user will be sent to upon succesful login, by default it is accounts/profile
LOGIN_REDIRECT_URL = 'home_page'

# The Redirect View the user will be sent to if they try to access content that requires being logged in, due to the @loginrequired decorator in users/views.py
# by default it is accounts/login

LOGIN_URL = 'login'


# MEDIA FILES #

# full path to where django will store uploaded files (images, etc.)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# public url of the directory, how we access the files through the browser
MEDIA_URL = '/media/'


#------------------------------------------------------------------------
#Email Setting...
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'futuresoftcode@gmail.com'
EMAIL_HOST_PASSWORD = 'Sul03314307703'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
#-------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# Number of seconds of inactivity before a user is marked offline
USER_ONLINE_TIMEOUT = 300

# Number of seconds that we will keep track of inactive users for before
# their last seen is removed from the cache
USER_LASTSEEN_TIMEOUT = 60 * 60 * 24 * 7

#---------------------------------------------------------------------
#Stripe Settings
STRIPE_SECRET_KEY = 'sk_test_jAndihGEFE8VtiRfUfTyygxH00JNgys3DY'
STRIPE_PUBLISHABLE_KEY = 'pk_test_7Caol5AeV11tgvLYCf7FlGXr00hMYbhIfm'