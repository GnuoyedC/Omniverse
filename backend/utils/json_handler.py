import requests
import warnings
import time
from typing import Dict,Any
from custom_warnings.json_handler_warnings import (
    KeyNotFoundInDictionaryWarning
)
from exceptions.json_handler_exceptions import (
    JsonHandlerNoUrlProvided,
    JsonHandlerRequestException,
    NotADictionaryException,
    MaxRetriesException
)

class JsonHandler:
    headers = {'Content-Type': 'application/json'}
    RATE_LIMIT_ERROR = 429
    RESPONSE_OK = 200
    @classmethod
    def get_json_from_url(cls, url:str) -> Dict[str,Any]:
        max_retries = 5
        wait_time = 1
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
        for attempt in range(max_retries):
            try:
                for attempt in range(max_retries):
                    time.sleep(1)
                    print(url, " is the url")
                    response = requests.get(url=url, headers=cls.headers, timeout=60)
                    if response.status_code == cls.RESPONSE_OK:
                        return response.json()
                    wait_time = int(response.headers.get('Retry-After', wait_time * 2))

            except requests.exceptions.RequestException as e:
                raise JsonHandlerRequestException(f"HTTP Request failed: {e}")
            print(f"Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
            wait_time *= 2  # exponential backoff

        raise MaxRetriesException()
    @classmethod
    def get_toplevel_keys(cls, json_dict: dict[str, Any]) -> list:
        """
        Retrieves names of all non-nested keys in a json dict.

        Args:
            json_dict (dict[str, Any]): Passed json dictionary.

        Returns:
            key_list (list): List of all key names.
        """

        key_list = []
        for _key in json_dict.keys():
            key_list.append(_key)
        return key_list

    @classmethod
    def get_all_keys(cls, json_dict: dict[str, Any]) -> list:
        """
        Retrieves names of all keys in a json dict.

        Args:
            json_dict (dict[str, Any]): Passed json dictionary.

        Returns:
            key_list (list): List of all key names.
        """
        if not isinstance(json_dict, dict):
            raise TypeError("Input is not a dictionary")  # Changed to TypeError for generality

        key_list = []
        for _key, _value in json_dict.items():
            key_list.append(_key)
            if isinstance(_value, dict):
                key_list.extend(cls.get_all_keys(_value))
            elif isinstance(_value, list):
                # Simplified list handling
                for item in _value:
                    if isinstance(item, dict):
                        key_list.extend(cls.get_all_keys(item))
        return key_list

    @classmethod
    def check_json_key(cls, key:str, json_object:dict[str,Any]):
        """
        checks if a key is in a dictionary.

        Args:
            key (str): target key.
            json_object (dict[str,Any]): target json dictionary to check.

        Raises:
            ValueError: _description_

        Returns:
            bool: True if key is in the dictionary.
        """
        if key not in cls.get_all_keys(json_object):
            warnings.warn(KeyNotFoundInDictionaryWarning(key=key))
        return True
