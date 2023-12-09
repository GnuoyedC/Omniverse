class NoHashableStringPassed(Exception):
    """
    Raised if either public key or private key is missing from params.

    Args:
        Exception (Exception):
    """
    def __init__(self,message="No hashable string passed."):
        self.message = message
        super().__init__(message)
