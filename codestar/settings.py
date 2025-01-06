"""
Django settings for codestar project.

Generated by 'django-admin startproject' using Django 4.2.17.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url



if os.path.isfile('env.py'):
    import env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent # Set the base directory for the project
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates') # Add the templates directory to the settings


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
                    'localhost',
                    '8000-nielmc-django-blog-tbkovgv7j0.us2.codeanyapp.com',
                    '.herokuapp.com',
                    '127.0.0.1',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', # Add the static files app to the list of installed apps
    'cloudinary_storage', # Add the cloudinary storage app to the list of installed apps
    'django.contrib.sites', # Add the sites app to the list of installed apps
    'allauth', # Add the allauth app to the list of installed apps
    'allauth.account', # Add the allauth account app to the list of installed apps
    'allauth.socialaccount', # Add the allauth social account app to the list of installed apps
    'crispy_forms', # Add the crispy forms app to the list of installed apps
    'crispy_bootstrap5', # Add the crispy bootstrap5 app to the list of installed apps
    'django_summernote', # Add the django summernote app to the list of installed apps
    'cloudinary', # Add the cloudinary app to the list of installed apps
    'blog', # Add the blog app to the list of installed apps
    'about', # Add the about app to the list of installed apps
]

SITE_ID = 1 # Add the site ID to the settings   
LOGIN_REDIRECT_URL = '/' # Add the login redirect URL to the settings
LOGOUT_REDIRECT_URL = '/' # Add the logout redirect URL to the settings

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Add whitenoise to the middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware', # Add the allauth account middleware to the middleware
]

ROOT_URLCONF = 'codestar.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR], # Add the templates directory to the settings
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

WSGI_APPLICATION = 'codestar.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# default settings with Django but not needed for this project as using POSTGRES
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

# List of trusted origis for requests which includes local development server URL
# and production server URL
CSRF_TRUSTED_ORIGINS = ['http://*.codeinstitute-ide.net/',
                        'https://*.herokuapp.com/',
                        'https://*codeanyapp.com/',
]

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

ACCOUNT_EMAIL_VERIFICATION = 'none' # Add the account email verification to the settings

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_DIRS = [os.path.join(BASE_DIR, 'static')] # Add the static directory to the settings
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # Add the staticfiles directory to the settings

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
