from .base import *

SECRET_KEY = (
    "django-insecure-8v88337#vy^_6hxdom1ex(9ke39c2idr_yqt&hd+on8&pz@wce"
)

DEBUG = False

ALLOWED_HOSTS = ["benben.pics", "api.benben.pics"]

DATABASES = {
    "default": {
        "ENGINE": config("DB_ENGINE"),
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
    }
}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
SECURE_HSTS_SECONDS = 86400
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
