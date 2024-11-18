from .base import *

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DEBUG = os.getenv("DJANGO_DEBUG", "") != "False"

ALLOWED_HOSTS = ["127.0.0.1"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}