import os
import django
import sys
from django.conf import settings
from custom_warnings.django_helper_warnings import (
    SetupAlreadyExists
)
import warnings
def config_exists() -> bool:
    """
    checks if config exists.

    Returns:
        bool: True if config exists already.
    """
    return settings.configured

def setup_django() -> str:
    """
    In an effort to quell redundancy
    I have created a setup function/helper file
    for setting up django in external scripts.

    Returns:
        settings (str): settings from django.conf
    """
    # Add the path to the 'backend' directory to the Python path
    if config_exists():
        warnings.warn(SetupAlreadyExists())
    else:
        script_dir = os.path.dirname(os.path.realpath(__file__))  # Path to utils/
        parent_dir = os.path.dirname(script_dir)  # Path to backend/
        sys.path.append(parent_dir)

        # Set up the Django environment
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'omniverse_drf.settings')
        django.setup()
        return settings