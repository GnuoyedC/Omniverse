import requests
from typing import Dict,Any
from exceptions.json_handler_exceptions import (
    JsonHandlerNoUrlProvided,
    JsonHandlerRequestException
)

class JsonHandler:
    headers = {'Content-Type': 'application/json'}
    @classmethod
    def get_json(cls,url) -> Dict[str,Any]:
        if url is None:
            raise JsonHandlerNoUrlProvided()
        try:
            response = requests.get(url,headers=cls.headers)
            response.raise_for_status() # Raises HTTPError for bad responses.
            return response.json()
        except requests.exceptions.RequestException as e:
            raise JsonHandlerRequestException(f"HTTP Request failed: {e}")