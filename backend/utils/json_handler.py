import requests
import ssl
ssl_context = ssl.create_default_context()
ssl_context.set_ciphers('DEFAULT@SECLEVEL=1')  # Example to lower security level
from typing import Dict,Any
from exceptions.json_handler_exceptions import (
    JsonHandlerNoUrlProvided,
    JsonHandlerRequestException
)

class JsonHandler:
    headers = {'Content-Type': 'application/json'}

    @classmethod
    def get_json_from_url(cls,url:str) -> Dict[str,Any]:
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
            """
            TODO: Fix the following:
                File "/Users/andromeda/development/projects/Omniverse/backend/utils/json_handler.py", line 39, in get_json_from_url
                    raise JsonHandlerRequestException(f"HTTP Request failed: {e}")
                exceptions.json_handler_exceptions.JsonHandlerRequestException: HTTP Request failed: HTTPSConnectionPool(host='gateway.marvel.com', port=443): Max retries exceeded with url: /v1/public/comics?format=hardcover&formatType=collection&limit=1&offset=0&apikey=f486ef2e851f918aad939b5e20582e09&hash=c738cbf94af57bdb79a69827bc5300ec&ts=1702070673.908445 (Caused by SSLError(SSLError(1, '[SSL: WRONG_SIGNATURE_TYPE] wrong signature type (_ssl.c:1006)')))
            """
            response = requests.get(url=url,headers=cls.headers,
                                    verify=False)
            response.raise_for_status() # Raises HTTPError for bad responses.
            return response.json()
        except requests.exceptions.RequestException as e:
            raise JsonHandlerRequestException(f"HTTP Request failed: {e}")

