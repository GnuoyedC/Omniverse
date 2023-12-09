from exceptions.hashify_exceptions import (
    NoHashableStringPassed
)
import hashlib

class Hashify:
    @staticmethod
    def md5hash(hashable_string:str) -> str:
        """
        Args:
            time (str): Timestamp (Epoch)
            private_key (str): Hashable string (in this context, private+public key)

        Raises:
            NoHashableStringPassed: If no string is passed, this is raised.

        Returns:
            str: Returns the hex digest of the hash object.
        """
        if hashable_string is None:
            raise NoHashableStringPassed()
        # Generate MD5 hash
        hash_object = hashlib.md5(hashable_string.encode())
        return hash_object.hexdigest()