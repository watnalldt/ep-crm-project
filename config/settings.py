"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from datetime import timedelta
from pathlib import Path

import environ
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    ALLOWED_HOSTS=(list, []),
    DEBUG=(bool, False),
    DEBUG_TOOLBAR=(bool, False),
    BROWSER_RELOAD=(bool, False),
    SENTRY_ENABLED=(bool, True),
)
env.read_env(str(BASE_DIR / ".env"))


SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS: list[str] = env("ALLOWED_HOSTS")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")
DEBUG_TOOLBAR = env("DEBUG_TOOLBAR")
BROWSER_RELOAD = env("BROWSER_RELOAD")



# Application definition

DJANGO_APPS = [
    "grappelli",  # grappelli admin
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]

THIRD_PARTY_APPS = [
    "import_export",
    "django_extensions",
    "crispy_forms",
    "crispy_bootstrap5",
    "django_filters",
    "admin_auto_filters",
    "rangefilter",
    "simple_history",
    "captcha",
    "user_visit",
    "axes",
]

PROJECT_APPS = [
    "users.apps.UsersConfig",
    "account_managers.apps.AccountManagersConfig",
    "client_managers.apps.ClientManagersConfig",
    "clients.apps.ClientsConfig",
    "contracts.apps.ContractsConfig",
    "utilities.apps.UtilitiesConfig",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware", # Whitenoise
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_auto_logout.middleware.auto_logout",  # Auto logout
    "user_visit.middleware.UserVisitMiddleware",  # User visit
    "simple_history.middleware.HistoryRequestMiddleware",  # History
    "axes.middleware.AxesMiddleware",  # Axes
]

# Enable the debug toolbar only in DEBUG mode.
if DEBUG and DEBUG_TOOLBAR:
    INSTALLED_APPS.append("debug_toolbar")
    MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
    INTERNAL_IPS = ["127.0.0.1"]

if DEBUG:
    INSTALLED_APPS.append("django_browser_reload")
    MIDDLEWARE.insert(0, "django_browser_reload.middleware.BrowserReloadMiddleware")


ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django_auto_logout.context_processors.auto_logout_client",  # Auto Logout
            ],
        },
    },
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {"default": env.db("DATABASE_URL")}
DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE")  # noqa F405


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Custom User Model
AUTH_USER_MODEL = "users.CustomUser"
LOGOUT_REDIRECT_URL = "users:login"

# Authentication
AUTHENTICATION_BACKENDS = [
    # AxesStandaloneBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    "axes.backends.AxesStandaloneBackend",
    # Django ModelBackend is the default authentication backend.
    "django.contrib.auth.backends.ModelBackend",
]
SITE_ID = 1
# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-gb"

TIME_ZONE = "Europe/London"

USE_I18N = True

USE_TZ = True
# UK Time Format
DATE_INPUT_FORMATS = ("%d/%m/%Y", "%d-%m-%Y")


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

DATA_UPLOAD_MAX_NUMBER_FIELDS = 25000
# Email Settings
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = env("EMAIL_USE_TLS")
ADMINS = [x.split(":") for x in env.list("DJANGO_ADMINS")]
MANAGERS = ADMINS
DEFAULT_FROM_EMAIL = env(
    "DJANGO_DEFAULT_FROM_EMAIL",
    default="Enquiries <david@energyportfolio.co.uk>",
)

# https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)

RECIPIENT_ADDRESS = env("RECIPIENT_ADDRESS")

# CACHES
# ------------------------------------------------------------------------------
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": env("REDIS_URL"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}
CACHE_TTL = 60 * 5

# SENTRY
if env("SENTRY_ENABLED"):
    sentry_sdk.init(
        dsn=env("SENTRY_DSN"),
        integrations=[
            DjangoIntegration(),
        ],
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0,
        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True,
    )

# Recaptcha
RECAPTCHA_PUBLIC_KEY = env("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = env("RECAPTCHA_PRIVATE_KEY")

# Auto Logout
AUTO_LOGOUT = {
    "IDLE_TIME": timedelta(minutes=1),
    "MESSAGE": "The session has expired. Please login again to  continue.",
    "REDIRECT_TO_LOGIN_IMMEDIATELY": True,
}

GRAPPELLI_ADMIN_TITLE = "Energy Portfolio Contract Management"

# axes configuration settings
AXES_FAILURE_LIMIT=3 # How many times a user can fail to log in
AXES_COOLOFF_TIME = timedelta(minutes=10) # How long before a user can fail to log in
AXES_LOCK_OUT_BY_COMBINATION_USER_AND_IP = True
# AXES_ONLY_USER_FAILURES=True # Block only on username
AXES_RESET_ON_SUCCESS = True # Reset failed login attempts after successful login
AXES_LOCKOUT_TEMPLATE = 'account_locked.html'
AXES_RESET_COOL_OFF_ON_FAILURE_DURING_LOCKOUT = False
