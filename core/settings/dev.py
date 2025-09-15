from .base import *

SECRET_KEY = (
    "django-insecure-8v88337#vy^_6hxdom1ex(9ke39c2idr_yqt&hd+on8&pz@wce"
)

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}
