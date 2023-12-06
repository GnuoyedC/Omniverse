from typing import Dict,Any
from django.conf import global_settings as settings
from exceptions.marvel_api_exceptions import (
    NoOmnibusIDProvidedException
)
from url_builder import URLBuilder as builder
from json_handler import JsonHandler as h_json
from time import time
from hashify import Hashify
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
    base_params = {
        "format": "hardcover",
        "formatType": "collection",
        "limit": 100,
        "offset": 0,
        "apikey": api_key
    }
    @classmethod
    def generate_hash(cls) -> tuple:
        ts = time()
        hashable_string = str(ts) + (cls.pvt_key + cls.api_key)
        hash = Hashify.md5hash(hashable_string)
        return hash, ts

    @classmethod
    def get_omnibus_by_id(cls, id: str) -> Dict:
        if id is None:
            raise NoOmnibusIDProvidedException()
        return {}
    @classmethod
    def test(cls):
        a = builder(cls.endpoint_url)
        hashish = cls.generate_hash()
        the_hash = hashish[0]
        the_ts = hashish[1]
        cls.base_params['hash'] = the_hash
        cls.base_params['ts'] = the_ts
        f = a.build(path=cls.path,
                params=cls.base_params)
        print(f)
        return
    @classmethod
    def get_all_omnibuses(cls) -> Dict[str,Any]:

        return {}
MarvelAPI.test()