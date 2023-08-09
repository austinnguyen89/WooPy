"""Settings module for WooPy.

This module contains the configuration settings for the WooPy project, including
WooCommerce API keys and database URI.
"""

import os

WOO_COMMERCE_API_KEY = os.environ.get(
    'WOO_COMMERCE_API_KEY', 'your_default_api_key')
WOO_COMMERCE_API_SECRET = os.environ.get(
    'WOO_COMMERCE_API_SECRET', 'your_default_api_secret')
WOO_COMMERCE_URL = os.environ.get('WOO_COMMERCE_URL', 'your_default_url')
DATABASE_URI = os.environ.get('DATABASE_URI', 'your_default_database_uri')
