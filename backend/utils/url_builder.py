from urllib.parse import (
    urlencode,
    urlparse,
    parse_qs
)
from exceptions.url_builder_exceptions import (
    NoPathPassedToBuild,
    InvalidURLPassed,
    NoURLPassedToParamUpdateFunction,
    NoParamPassedToParamUpdateFunction,
    NoValuePassedToParamUpdateFunction,
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
            raise InvalidURLPassed(url)

    def update_params(self, url:str, param:str, value:str):
        """
        Updates specific parameters for a passed URL.

        Args:
            url (str): The passed encoded URL.
            param (str): the parameter you want to modify.
            value (str): the value for that parameter.

        Returns:
            str: Returns the encoded, modified URL with updated params.
        """
        if not url:
            raise NoURLPassedToParamUpdateFunction()
        if not param:
            raise NoParamPassedToParamUpdateFunction()
        if not value:
            raise NoValuePassedToParamUpdateFunction()

        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        query_params[param] = value
        query_string = urlencode(query_params,doseq=True)
        return parsed_url._replace(query=query_string).geturl()

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