import os
from django.utils.translation import gettext_lazy as _


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import environ

env = environ.Env(
    STRIPE_PUBLISHABLE_KEY= (str),
    STRIPE_SECRET_KEY = (str),
    STRIPE_WEBHOOK_SECRET = (str),


    REDIS_HOST = (str),
    REDIS_PORT =(int),
    REDIS_DB = (int),
)


GTK_FOLDER = r'C:\Program Files\GTK3-Runtime Win64\bin'
os.environ['PATH'] = GTK_FOLDER + os.pathsep + os.environ.get('PATH', '')
environ.Env.read_env(BASE_DIR + '/.env')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#70en)0(b7agjhjzau+zu1z6@*ov4^-h(@+h63h7(iqd2yrq-o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'localflavor',
    'rosetta',
    'shop',
    'cart',
    'orders',
    'payment',
    'parler',
    'coupons',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myshop.urls'

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
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'myshop.wsgi.application'


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

LANGUAGE_CODE = 'en'

LANGUAGES = [
 ('en', _('English')),
 ('es', _('Spanish')),
]

# настройки django-parler
PARLER_LANGUAGES = {
 None: (
    {'code': 'en'},
    {'code': 'es'},
 ),
 'default': {
    'fallback': 'en',
    'hide_untranslated': False,
 }
}



LOCALE_PATHS = [
 BASE_DIR + 'locale',
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CART_SESSION_ID = 'cart'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR + '/static'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR + 'media'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Настроечные параметры Stripe
STRIPE_PUBLISHABLE_KEY = env('STRIPE_PUBLISHABLE_KEY') # Публикуемый ключ
STRIPE_SECRET_KEY = env('STRIPE_SECRET_KEY')# Секретный ключ
STRIPE_API_VERSION = '2022-08-01'
STRIPE_WEBHOOK_SECRET = env('STRIPE_WEBHOOK_SECRET')


# настроечные параметры Redis
REDIS_HOST = env('REDIS_HOST')
REDIS_PORT = env('REDIS_PORT')
REDIS_DB = env('REDIS_DB')


