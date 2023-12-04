class NoOmnibusIDProvidedException(Exception):
    """Exception raised for no omnibus ID provided.

    Attributes:
        message -- indicates that the omnibus ID was not provided.
    """

    def __init__(self, message="Omnibus ID not provided."):
        self.message = message
        super().__init__(self.message)