import sys
import os
import django

# Add the path to the 'backend' directory to the Python path
script_dir = os.path.dirname(os.path.realpath(__file__))  # Path to utils/
parent_dir = os.path.dirname(script_dir)  # Path to backend/
sys.path.append(parent_dir)

# Set up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'omniverse_drf.settings')
django.setup()
# Now you can import Django settings and other Django-related modules
from django.conf import settings

# Your existing imports and code
# ...

from typing import Dict,Any
from exceptions.marvel_api_exceptions import (
    NoOmnibusIDProvidedException
)

from url_builder import URLBuilder as builder
from json_handler import JsonHandler as h_json
from time import time
from hashify import Hashify
import os
import django

# Now you can use your utility function
# All calls to the Marvel Comics API must pass your public key via an “apikey”
# parameter. Client-side and server-side applications have slightly different
# authentication rules in order to access the API. Please read below for the
# appropriate method for your application.
# REF: https://developer.marvel.com/documentation/authorization
# REF2: https://developer.marvel.com/docs
# Example: https://gateway.marvel.com:443/v1/public/comics?format=hardcover&formatType=collection&limit=100&apikey=

class MarvelAPI:
    path = "comics"
    # endpoint_url = settings.MARVEL_API_ENDPOINT
    api_key = settings.MARVEL_API_KEY
    pvt_key = settings.MARVEL_PVT_KEY
    endpoint_url = settings.MARVEL_API_ENDPOINT
    base_params = {
        "format": "hardcover",
        "formatType": "collection",
        "limit": 100,
        "offset": 0,
        "apikey": api_key
    }
    @classmethod
    def generate_hash(cls) -> tuple:
        """
        Generates a hash for the API.

        Returns:
            tuple: contains the hash value and the time stamp.
        """
        ts = time()
        hashable_string = str(ts) + (cls.pvt_key + cls.api_key)
        hash = Hashify.md5hash(hashable_string)
        return hash, ts

    @classmethod
    def get_base_url_urlbuild(cls) -> tuple:
        """
        Gets the base API URL,
        returns URL builder and URL.

        Returns:
            tuple: urlbuilder, url
        """
        urlbuild = builder(cls.endpoint_url)
        hashish = cls.generate_hash()
        hash = hashish[0]
        ts = hashish[1]
        cls.base_params['hash'] = hash
        cls.base_params['ts'] = ts
        url = urlbuild.build(cls.path,
                            **cls.base_params)
        return urlbuild, url
    @classmethod
    def get_omnibus_by_id(cls, id: str) -> Dict:
        if id is None:
            raise NoOmnibusIDProvidedException()
        return {}

    @classmethod
    def get_upcoming_omnibuses(cls) -> Dict[str,Any]:
        return

    @classmethod
    def get_omnibus_all_count(cls) -> int:
        url = builder(cls.endpoint_url)
        return

    @classmethod
    def get_all_omnibuses(cls) -> Dict[str,Any]:
        """
        returns all omnibuses up to 100.

        Returns:
            Dict[str,Any]: _description_
        """
        return {}
    @classmethod
    def test(cls):
        urlbuild, url = cls.get_base_url_urlbuild()

        f = urlbuild.update_params(url=url,param="limit",value="1")
        print(f)
        return
if __name__ == "__main__":
    MarvelAPI.test()