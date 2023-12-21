class JsonHandlerNoUrlProvided(Exception):
    """Exception raised for no url provided to json handler.

    Attributes:
        message -- indicates that the json handler url was not provided.
    """

    def __init__(self, message="URL not provided to JsonHandler"):
        self.message = message
        super().__init__(message)

class JsonHandlerRequestException(Exception):
    """
    Exception raised for any issues with HTTP requests in the JSON
    handler request.
    """
    def __init__(self, message="There was an issue with the request."):
        self.message = message
        super().__init__(message)

class NotADictionaryException(Exception):
    """
    Exception raised if value passed is not a
    valid dictionary.
    """
    def __init__(self,message="Not a valid dictionary"):
        self.message = message
        super().__init__(message)
class MaxRetriesException(Exception):
    """
    _summary_

    Args:
        Exception (_type_): _description_
    """
    def __init__(self,message="Max retries reached"):
        self.message = message
        super().__init__(message)