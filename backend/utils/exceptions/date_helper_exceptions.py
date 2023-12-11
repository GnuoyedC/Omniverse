class DayNotValidForMonth(Exception):

    def __init__(self, message="Day must be valid for month specified."):
        self.message = message
        super().__init__(message)