"""Settings module for WooPy.

This module contains the configuration settings for the WooPy project, including
WooCommerce API keys and database URI. It also includes validation to ensure that
all required environment variables are set.

Environment Variables:
    WOO_COMMERCE_API_KEY: The API key for WooCommerce integration.
    WOO_COMMERCE_API_SECRET: The API secret for WooCommerce integration.
    WOO_COMMERCE_URL: The URL for WooCommerce.
    DATABASE_URI: The URI for the database connection.
"""

import os


def get_env_variable(var_name, default=None, required=False):
    """Retrieve and validate an environment variable.

    Args:
        var_name (str): The name of the environment variable.
        default: The default value if the environment variable is not set.
        required (bool): Whether the environment variable is required.

    Returns:
        The value of the environment variable.

    Raises:
        ValueError: If the environment variable is required but not set.
    """
    value = os.environ.get(var_name, default)
    if value is None and required:
        raise ValueError(f"{var_name} must be set")
    return value


WOO_COMMERCE_API_KEY = get_env_variable('WOO_COMMERCE_API_KEY', required=True)
WOO_COMMERCE_API_SECRET = get_env_variable(
    'WOO_COMMERCE_API_SECRET', required=True)
WOO_COMMERCE_URL = get_env_variable('WOO_COMMERCE_URL', required=True)
DATABASE_URI = get_env_variable('DATABASE_URI', required=True)
