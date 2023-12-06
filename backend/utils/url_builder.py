from urllib.parse import (
    urlencode,
    urlparse
)
from utils.exceptions.url_builder_exceptions import (
    NoPathPassedToBuild,
    InvalidURLPassed
)

class URLBuilder:
    def __init__(self,base_url:str):
        # Normalizes the URL by removing
        # slashes at the end.
        self.base_url = base_url.rstrip('/')
        self.validate_url(self.base_url)
    def validate_url(self, url:str) -> None:
        """
        Validates a URL.

        Args:
            url (str): URL as a string.

        Returns:
            None: Raises an exception if the URL is invalid.
        """
        parsed_url = urlparse(url)
        if not all([parsed_url.scheme,parsed_url.netloc]):
            raise InvalidURLPassed()

    def build(self,path:str,**params) -> str:
        """
        Builds a URL from a passed path and
        a dict of parameters.

        Args:
            path (str): the URL root.
            params (dict): dictionary of parameters.

        Raises:
            NoPathPassedToBuild: raised if no path is passed.
            NoParamsPassedToBuild: raised if no params are passed.

        Returns:
            url (str): the final url.
        """

        if not path:
            raise NoPathPassedToBuild()

        if not params:
            return f"{self.base_url}/{path.lstrip('/')}"

        query_string = urlencode(params)
        url = f"{self.base_url}/{path.lstrip('/')}?{query_string}"
        return url