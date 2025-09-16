from pathlib import Path
from pathlib import Path
import os   # sabse upar likh


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'replace-this-with-a-secret-key'

DEBUG = True

ALLOWED_HOSTS = [
    'campusforces.in',           # Tumhara custom domain
    'www.campusforces.in',       # Custom domain with www
    'campusforce-django.onrender.com',  # Render ka default domain
    '127.0.0.1',                 # Localhost (testing ke liye)
    'localhost'                  # Localhost alternate
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]


AUTH_USER_MODEL = 'accounts.CustomUser'
 
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'campusforce.urls'

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

WSGI_APPLICATION = 'campusforce.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'campusforce_db',
#         'USER': 'root',
#         'PASSWORD': 'toor',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'railway',  # yeh hi aapka DB name hai
        'USER': 'root',     # aapke command me diya hai
        'PASSWORD': 'bnnZhBIpNIJktddEyNLchoXiuoZRruGR',  # yeh hai password
        'HOST': 'gondola.proxy.rlwy.net',  # host
        'PORT': '40541',   # port
    }
}



MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

RAZORPAY_KEY_ID = "rzp_test_tV8hhS0olbbfGd"
RAZORPAY_SECRET_KEY = "bLZMe2pOY0hqOysqLAZriZoX"


AUTH_USER_MODEL = 'accounts.CustomUser'
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/accounts/login/' 

INSTALLED_APPS += [
    'accounts',
]

AUTH_USER_MODEL = 'accounts.CustomUser'


AUTH_USER_MODEL = 'accounts.CustomUser'

# Email ke liye SMTP setup (OTP & Reset Password)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'noreplycampusforces@gmail.com'
EMAIL_HOST_PASSWORD = 'pkwm yfbo ppgq nfsg'
EMAIL_USE_TLS = True


AUTH_USER_MODEL = 'accounts.CustomUser'

# INSTALLED_APPS is already defined above and extended with 'accounts', so this redefinition is removed to avoid syntax errors.


AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

BASE_DIR = Path(__file__).resolve().parent.parent

# STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR / "core/static"]   # development ke liye
# STATIC_ROOT = BASE_DIR / "staticfiles"          # collectstatic ke liye


STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "core/static",
]

# yaha double quotes hata ke BASE_DIR ke andar proper folder banade
STATIC_ROOT = os.path.join(str(BASE_DIR), "staticfiles")


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# TEMPLATE DIR setup
TEMPLATES[0]['DIRS'] = [os.path.join(BASE_DIR, 'templates')]
