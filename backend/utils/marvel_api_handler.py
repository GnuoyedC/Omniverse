from typing import Dict,Any
from django.conf import settings
from utils.exceptions.marvel_api_exceptions import (
    NoOmnibusIDProvidedException
)
from url_builder import URLBuilder as builder
from utils.json_handler import JsonHandler as h_json
from hashify import Hashify as hasher
# All calls to the Marvel Comics API must pass your public key via an “apikey”
# parameter. Client-side and server-side applications have slightly different
# authentication rules in order to access the API. Please read below for the
# appropriate method for your application.
# REF: https://developer.marvel.com/documentation/authorization
# REF2: https://developer.marvel.com/docs
# Example: https://gateway.marvel.com:443/v1/public/comics?format=hardcover&formatType=collection&limit=100&apikey=

class MarvelAPI:
    path = "comics"
    endpoint_url = settings.MARVEL_API_ENDPOINT
    api_key = settings.MARVEL_API_KEY
    pvt_key = settings.MARVEL_PVT_KEY
    hashed_key = hasher.md5hash(pvt_key,api_key)

    omni_dict = {}
    @classmethod
    def get_omnibus_by_id(cls,id:str) -> Dict:
        if id is None:
            raise NoOmnibusIDProvidedException()

        return {}

    @classmethod
    def get_all_omnibuses(cls) -> Dict[str,Any]:

        return {}