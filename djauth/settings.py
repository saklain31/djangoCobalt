import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'to4)2gq5-*r_g75guof)c@g^htwy1w_amwh)$-=t)g^ipr%et#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

MY_KEY = 'AIzaSyCZj-I8lG27P2QkBhWE1jEtohd-3JIsIw4'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'SocialAuth',
    'easy_maps',
    # 'cms',
    'user.apps.UserConfig',


    'django.contrib.sites', # added for allauth
    'allauth', # added for allauth
    'allauth.account', # new added for allauth
    'allauth.socialaccount', # new added for allauth
    'allauth.socialaccount.providers.github', # new added for allauth Github
    'allauth.socialaccount.providers.facebook', #new added for allauth Facebook
    'allauth.socialaccount.providers.google', #new added for gmail authentication


    'rolepermissions',
    'guardian',
    'countdown',
    'event',

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

AUTHENTICATION_BACKENDS = [
        'social_core.backends.facebook.FacebookOAuth2',
        'social_core.backends.google.GoogleOAuth2',

        'django.contrib.auth.backends.ModelBackend',
        'allauth.account.auth_backends.AuthenticationBackend', #allauth authentication background system

        'guardian.backends.ObjectPermissionBackend', #role permission guardian backend

    ]

ROOT_URLCONF = 'djauth.urls'

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

                'social_django.context_processors.backends', # add this
                'social_django.context_processors.login_redirect', # add this

            ],
        },
    },
]

WSGI_APPLICATION = 'djauth.wsgi.application'




# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cobalt',
        'USER': 'cobalt_admin',
        'PASSWORD': 'colbalt_XYZ_pass',
        'HOST': 'localhost',
        'PORT': '',
    }
}



# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

LOGIN_URL = 'login' #'/auth/login/google-oauth2/'
LOGIN_REDIRECT_URL = 'home'
#LOGIN_REDIRECT_URL = '/cms/home/'
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = 'login' #after log in where we will redirect

#FACEBOOK
SOCIAL_AUTH_FACEBOOK_KEY = '425400614856221'
SOCIAL_AUTH_FACEBOOK_SECRET = '781a4da519cadd47dd3e286af4ee6ce1'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_link']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'fields': 'id, name, email, picture.type(large), link'
}
SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [
    ('name', 'name'),
    ('email', 'email'),
    ('picture', 'picture'),
    ('link', 'profile_url'),
    ]

#GOOGLE
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '259861524975-enubc8ciita9krv3paag2b5q1tcghn5l.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'uX__wKV12DBQLxXBho6yJokP'

SOCIAL_AUTH_URL_NAMESPACE = 'social'

EASY_MAPS_GOOGLE_KEY = 'AIzaSyBnl5PYgBzmrMakPcq8RFbaIyH3yRg6YmM'
# EASY_MAPS_CENTER = (-41.3, 32)



# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/



# Static files
BASE_DIR_UP = os.path.dirname(BASE_DIR)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'


# Media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

#FOR AUTH MODULE
# https://stackoverflow.com/questions/15409366/django-socialapp-matching-query-does-not-exist
# important issue regarding SITE_ID
SITE_ID = 2


# For social account django all auth
# http://www.sarahhagstrom.com/2013/09/the-missing-django-allauth-tutorial/
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

SOCIALACCOUNT_QUERY_EMAIL = True

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'oauth2',
        'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
        'SCOPE': ['email', 'public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time',
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': lambda request: 'en_US',   #path.to.callable  #issue: https://stackoverflow.com/questions/16589661/django-allauth-does-not-find-accounts-login-view-due-to-no-module-named-path-t
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.12',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_UNIQUE_EMAIL = True

# Role permission module
ROLEPERMISSIONS_MODULE = 'djauth.roles'
