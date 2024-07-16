import os
import dj_database_url
from decouple import config
from pathlib import Path
from whitenoise.storage import CompressedManifestStaticFilesStorage
import re

class WhiteNoiseStaticFilesStorage(CompressedManifestStaticFilesStorage):
    ignored_files = [
        re.compile(r'^assets/fonts/HKGrostesk.*'),
        re.compile(r'^assets/fonts/hkgrotesk.*'),
        re.compile(r'^assets/css/app\.min\.css$'),
    ]

    def hashed_name(self, name, content=None, filename=None):
        # Ignore files in the ignored_files list
        for ignored in self.ignored_files:
            if ignored.match(name):
                return name
        
        # Process images only from your specific folder
        if name.startswith('assets/images/'):
            return super().hashed_name(name, content, filename)
        
        # For other image files, return the original name without processing
        if name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg')):
            return name
        
        # Process other files normally
        return super().hashed_name(name, content, filename)
    
    def post_process(self, *args, **kwargs):
        files = super().post_process(*args, **kwargs)
        for name, hashed_name, processed in files:
            if not name.endswith('app.min.css'):
                yield name, hashed_name, processed

#WHITENOISE_EXCLUDE_PATHS = ['/assets/css/app.min.css']

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$-(s*^93$^1v1cq-pb6ef4f(euz^)vyrebiieh3_q17qbtsbj!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['.vercel.app', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Expenses',
    'Authentication',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'System.urls'

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

WSGI_APPLICATION = 'System.wsgi.application'
AUTH_USER_MODEL = 'Authentication.User'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ExpenseDB',     
        'USER': 'postgres',      
        'PASSWORD': 'P@ssw0rd',  
        'HOST': 'localhost',              
        'PORT': '5432',                  
    }
}

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "static", "assets", "libs")
]

#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_STORAGE = 'System.settings.WhiteNoiseStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
