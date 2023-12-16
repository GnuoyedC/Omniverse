class KeyNotFoundInDictionaryWarning(Warning):
    def __init__(self,key):
        self.key = key
        super().__init__(message=f"Key not found: {key}")