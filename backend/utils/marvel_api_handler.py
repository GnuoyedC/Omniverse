from typing import Dict,Any,List
from json_handler import JsonHandler as h_json
from url_builder import URLBuilder as builder
from time import time
from hashify import Hashify
from date_helpers import (
    get_current_date,
    get_current_date_time,
    get_future_date
)
from exceptions.marvel_api_exceptions import (
    NoOmnibusIDProvidedException,
    OmnibusCountIsZero,
    DataCountIsZero
)
import django
from django_helper import setup_django
# All calls to the Marvel Comics API must pass your public key via an “apikey”
# parameter. Client-side and server-side applications have slightly different
# authentication rules in order to access the API. Please read below for the
# appropriate method for your application.
# REF: https://developer.marvel.com/documentation/authorization
# REF2: https://developer.marvel.com/docs
# Example: https://gateway.marvel.com:443/v1/public/comics?format=hardcover&formatType=collection&limit=100&apikey=

# Note: I believe Marvel API hasn't been updated to reflect modern REST API
# standards, so you will require a version of urllib that does not have its
# SSL/TLS functionality deprecated (i.e. urllib3 < 2.1.0), in this case 1.26.16

SETTINGS = setup_django()
class MarvelAPI:
    path = "comics"
    api_key = SETTINGS.MARVEL_API_KEY
    pvt_key = SETTINGS.MARVEL_PVT_KEY
    endpoint_url = SETTINGS.MARVEL_API_ENDPOINT
    base_params = {
        "limit": 100,
        "offset": 0,
        "apikey": api_key
    }
    POLLING_MAX = 2000
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
        hash,ts = cls.generate_hash()
        _params = cls.base_params
        _params['hash'] = hash
        _params['ts'] = ts
        url = urlbuild.build(cls.path,
                            **_params)
        return urlbuild, url
    @classmethod
    def get_all_comics_count(cls) -> int:
        """
        Retrieves the total count of all omnibuses
        from the API.

        Returns:
            result (int): the total amount of omnibuses available.
        """
        urlbuild, url = cls.get_base_url_urlbuild()
        _url = builder.update_params(url=url,param="limit",value="1")
        return h_json.get_json_from_url(url=_url)['data']['total']
    @classmethod
    def get_all_comics(cls) -> List[Dict[str,Any]]:
        """
        retrieves all comics from the Marvel API.
        Returns:
            Dict[str,Any]: comics json dict.
        """
        result_list = []
        comic_all_count = cls.get_all_comics_count()
        if comic_all_count == 0:
            raise DataCountIsZero()

        first_comic = 0
        last_comic = comic_all_count
        offset_step = 100
        urlbuild, url = cls.get_base_url_urlbuild()

        for comic_offset in range(first_comic,
                            last_comic,
                            offset_step):
            _url = builder.update_params(url=url,
                                         param="offset",
                                         value=f"{comic_offset}")
            result_list.extend(h_json.get_json_from_url(url=_url)['data']['results'])

        return result_list

    @classmethod
    def get_comics_passed_params(cls, offset:int,
    poll_limit: int) -> List[Dict[str,Any]]:
        """
        _summary_
        Args:
            start (int): what position of the data to start at.
            offset (int): position from the start.
            limit (int): amount to return in result set.
            data_count (int): amount of data in total.
        Raises:
            DataCountIsZero: if data count is zero, raised.
        Returns:
            List[Dict[str,Any]]: returns list of JSON dicts.
        """
        result_list = []

        if poll_limit == 0:
            raise DataCountIsZero()
        urlbuild, url = cls.get_base_url_urlbuild()

        start = offset
        offset_step = cls.base_params['limit']
        end = poll_limit + start
        # so say we are only polling a max of 2000 records at a time,
        # which would be the polling limit.
        # the offset is basically the record number in that data we start with.
        # if we start with 0 as the offset,
        # the step is going to be 100,
        # and the end is going to be the poll limit + the start position.

        for data_offset in range(start,
                            end,
                            offset_step):
            _url = builder.update_params(url=url,
                                         param="offset",
                                         value=f"{data_offset}")
            result_list.extend(h_json.get_json_from_url(url=_url)['data']['results'])
        return result_list

    @classmethod
    def get_marvel_comic_updates_since(cls, since_date:str) -> List[dict[str,Any]]:
        """
        _summary_

        Args:
            since_date (str): _description_

        Returns:
            List[dict[str,Any]]: _description_
        """
        # urlbuild, url = cls.get_base_url_urlbuild()
        # _url = builder.update_params(url=url,param="modifiedSince",
        #                             value=f"{since_date}")

        # return h_json.get_json_from_url(url=_url)['data']['results']
        result_list = []
        comics_since_count = cls.get_latest_comics_count(since_date=since_date)
        print(comics_since_count, " is the comics since count")
        if comics_since_count == 0:
            raise DataCountIsZero()
        urlbuild, url = cls.get_base_url_urlbuild()
        _url = builder.update_params(url=url,param="modifiedSince",
                                    value=f"{since_date}")
        offset_step = (cls.POLLING_MAX if
                        comics_since_count >= cls.POLLING_MAX
                        else cls.base_params['limit'])
        # so say we are only polling a max of 2000 records at a time,
        # which would be the polling limit.
        # the offset is basically the record number in that data we start with.
        # if we start with 0 as the offset,
        # the step is going to be 100,
        # and the end is going to be the poll limit + the start position.
        first_comic = 0
        last_comic = comics_since_count

        for data_offset in range(first_comic,
                            last_comic,
                            offset_step):
            _url = builder.update_params(url=_url,
                                         param="offset",
                                         value=f"{data_offset}")
            result_list.extend(h_json.get_json_from_url(url=_url)['data']['results'])
        return result_list
    @classmethod
    def get_omnibus_by_id(cls, id: str) -> Dict:
        if id is None:
            raise NoOmnibusIDProvidedException()
        return {}

    @classmethod
    def get_upcoming_omnibuses(cls) -> str:
        """
        Retrieves all future omnibus releases available.
        Returns:
        """
        current_date = get_current_date()
        urlbuild, url = cls.get_base_url_urlbuild()
        _url = builder.update_params(url=url,param="dateRange",
                                     value=f"{current_date},{get_future_date()}")
        return _url
    @classmethod
    def get_latest_comics_count(cls,since_date:str) -> int:
        urlbuild, url = cls.get_base_url_urlbuild()
        _url = builder.update_params(url=url,param="modifiedSince",value=f"{since_date}")
        _url = builder.update_params(url=_url,param="limit",value="1")
        result = h_json.get_json_from_url(url=_url)['data']['total']
        return result
    @classmethod
    def get_omnibus_all_count(cls) -> int:
        """
        Retrieves the total count of all omnibuses
        from the API.
        Returns:
            result (int): the total amount of omnibuses available.
        """
        urlbuild, url = cls.get_base_url_urlbuild()
        _url = builder.update_params(url=url,param="limit",value="1")
        result = h_json.get_json_from_url(url=_url)['data']['total']
        return result

    @classmethod
    def get_all_omnibuses(cls) -> List[Dict[str,Any]]:
        """
        retrieves all omnibuses from the Marvel API.
        Returns:
            Dict[str,Any]: _description_
        """
        result_list = []
        omnibus_all_count = cls.get_omnibus_all_count()
        if omnibus_all_count == 0:
            raise OmnibusCountIsZero()

        first_omnibus = 0
        last_omnibus = omnibus_all_count
        limit = offset_step = 100
        urlbuild, url = cls.get_base_url_urlbuild()

        for omnibus_offset in range(first_omnibus,
                            last_omnibus,
                            offset_step):
            _url = builder.update_params(url=url,
                                         param="offset",
                                         value=f"{omnibus_offset}")
            result_list.extend(h_json.get_json_from_url(url=_url)['data']['results'])

        return result_list
    @classmethod
    def get_single_omnibus(cls):
        """
        gets a single omnibus entry.
        """
        result_list = []
        urlbuild, url = cls.get_base_url_urlbuild()
        _url = builder.update_params(url=url,
                                     param="limit",
                                     value="1")
        result_list.extend(h_json.get_json_from_url(url=_url)['data']['results'])
        return result_list
if __name__ == "__main__":
    MarvelAPI.get_base_url_urlbuild()