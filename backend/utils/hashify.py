from exceptions.hashify_exceptions import (
    NoHashableStringPassed
)
from time import time
import hashlib

class Hashify:
    @staticmethod
    def md5hash(string:str) -> str:
        """
        Args:
            string (str): Hashable string (in this context, private+public key)

        Raises:
            NoHashableStringPassed: If no string is passed, this is raised.

        Returns:
            str: Returns the hex digest of the hash object.
        """
        if not string:
            raise NoHashableStringPassed()
        hashable_string = str(time()) + string
        # Generate MD5 hash
        hash_object = hashlib.md5(hashable_string.encode())
        return hash_object.hexdigest()