import requests
from typing import Dict,Any
from exceptions.json_handler_exceptions import (
    JsonHandlerNoUrlProvided,
    JsonHandlerRequestException
)

class JsonHandler:
    headers = {'Content-Type': 'application/json'}
    @classmethod
    def get_json(cls,url:str) -> Dict[str,Any]:
        """
        A function that makes a request to a passed
        URL to retrieve JSON.

        Args:
            url (str): URL string.

        Raises:
            JsonHandlerNoUrlProvided: thrown if no URL is provided.
            JsonHandlerRequestException: thrown if anything is wrong with
            the HTTP request.

        Returns:
            Dict[str,Any]: JSON response
        """
        if url is None:
            raise JsonHandlerNoUrlProvided()
        try:
            response = requests.get(url,headers=cls.headers)
            response.raise_for_status() # Raises HTTPError for bad responses.
            return response.json()
        except requests.exceptions.RequestException as e:
            raise JsonHandlerRequestException(f"HTTP Request failed: {e}")