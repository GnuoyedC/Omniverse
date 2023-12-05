from utils.exceptions.url_builder_exceptions import (
    NoPathPassedToBuild,
    NoParamsPassedToBuild
)
class URLBuilder:
    def __init__(self,base_url):
        self.base_url = base_url
        return
    def build(self,path,**params) -> str:
        """
        Builds a URL from a passed path and
        a dict of parameters.

        Args:
            path (str): the URL root.

        Raises:
            NoPathPassedToBuild: raised if no path is passed.
            NoParamsPassedToBuild: raised if no params are passed.

        Returns:
            str: the final url.
        """
        if not path:
            raise NoPathPassedToBuild()
        if not params:
            raise NoParamsPassedToBuild()

        return