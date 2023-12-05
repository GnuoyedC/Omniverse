class NoPathPassedToBuild(Exception):
    """Exception raised for no path provided.

    Attributes:
        message -- indicates that no path was  passed.
    """

    def __init__(self, message="No path passed to URL builder."):
        self.message = message
        super().__init__(self.message)

class NoParamsPassedToBuild(Exception):
    """Exception raised for no parameters provided.

    Attributes:
        message -- indicates that no parameters were passed.
    """

    def __init__(self, message="No params passed to URL builder."):
        self.message = message
        super().__init__(self.message)

