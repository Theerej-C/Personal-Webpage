import os

# Set the default settings module based on an environment variable
ENVIRONMENT = os.getenv('DJANGO_ENV', 'development')  # Default to 'development'

if ENVIRONMENT == 'production':
    from .settings_prod import *
else:
    from .settings_dev import *