from .base import *
from decouple import config

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

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
SECURE_HSTS_SECONDS = 86400
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


SWAGGER_SETTINGS = {
    "USE_SESSION_AUTH": False,  # hide the Django login/logout in Swagger UI
    "SECURITY_DEFINITIONS": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": 'JWT Authorization header using the Bearer scheme. '
                           'Example: "Authorization: Bearer <your_token>"',
        }
    },
}