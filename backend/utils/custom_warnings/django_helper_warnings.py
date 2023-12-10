class SetupAlreadyExists(Warning):
    def __init__(self,message="Django setup already exists."):
        self.message = message
        super().__init__(message)