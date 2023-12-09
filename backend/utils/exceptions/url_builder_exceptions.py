class NoPathPassedToBuild(Exception):
    """
    Exception raised for no path provided.
    """
    def __init__(self, message="No path passed to URL builder."):
        self.message = message
        super().__init__(self.message)

class NoParamsPassedToBuild(Exception):
    """
        Exception raised for no parameters provided.
    """
    def __init__(self, message="No params passed to URL builder."):
        self.message = message
        super().__init__(self.message)

class InvalidURLPassed(Exception):
    """
    Exception raised for no URL provided.
    """
    def __init__(self, url:str):
        self.url = url
        self.message = f"Invalid URL passed: {url}"
        super().__init__(self.message)

class NoURLPassedToParamUpdateFunction(Exception):
    """
    Raised if no url is passed to the param update function.
    """
    def __init__(self,message="No URL passed to param update function."):
        self.message = message
        super().__init__(self.message)

class NoParamPassedToParamUpdateFunction(Exception):
    """
    Raised if no parameter is passed to param update function.
    """
    def __init__(self,message="No param passed to param update function."):
        self.message = message
        super().__init__(self.message)
class NoValuePassedToParamUpdateFunction(Exception):
    """
    No value passed to parameter update function.
    """
    def __init__(self,message="No value passed to param update function."):
        self.message = message
        super().__init__(self.message)