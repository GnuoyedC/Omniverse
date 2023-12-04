from typing import Dict
from django.conf import settings
from utils.exceptions.marvel_api_exceptions import (
    NoOmnibusIDProvidedException)

# All calls to the Marvel Comics API must pass your public key via an “apikey”
# parameter. Client-side and server-side applications have slightly different
# authentication rules in order to access the API. Please read below for the
# appropriate method for your application.
# REF: https://developer.marvel.com/documentation/authorization
# REF2: https://developer.marvel.com/docs
class MarvelAPI:
    endpoint_url = settings.MARVEL_API_ENDPOINT
    api_key = settings.MARVEL_API_KEY

    @classmethod
    def get_omnibus_by_id(cls,id) -> Dict:
        if id is None:
            raise NoOmnibusIDProvidedException

        return {}

    @classmethod
    def get_all_omnibuses(cls) -> Dict:
        return {}