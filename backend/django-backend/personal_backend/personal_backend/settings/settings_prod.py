from .settings_base import *

# Production-specific settings
DEBUG = False  # Disable debug mode in production

# Set allowed hosts for production
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'your-production-domain.com').split(',')

# Restrict CORS to specific origins in production
CORS_ALLOWED_ORIGINS = [
    "https://your-production-domain.com",  # Production frontend
    "https://another-allowed-origin.com",  # Add any other allowed origins
]