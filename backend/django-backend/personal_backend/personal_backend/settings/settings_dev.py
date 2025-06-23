from .settings_base import *

# Development-specific settings
DEBUG = True  # Enable debug mode for development

# Allow all origins for development
CORS_ALLOW_ALL_ORIGINS = True  # Allow all origins for development


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': '5432',
    }
}
# Additional development settings can be added here