class NoOmnibusIDProvidedException(Exception):
    """Exception raised for no omnibus ID provided.

    Attributes:
        message -- indicates that the omnibus ID was not provided.
    """

    def __init__(self, message="Omnibus ID not provided."):
        self.message = message
        super().__init__(message)

class OmnibusCountIsZero(Exception):
    """Exception raised if there are no omnibuses available.

    Attributes:
        message -- indicates that no omnibuses are returned.
    """

    def __init__(self, message="Omnibus count is 0."):
        self.message = message
        super().__init__(message)

class DataCountIsZero(Exception):
    """Exception raised if no data is available.

    Attributes:
        message -- indicates that no data are returned.
    """

    def __init__(self, message="Data count is 0."):
        self.message = message
        super().__init__(message)