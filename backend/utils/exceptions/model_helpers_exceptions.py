class ModelNotPassed(Exception):
    """
    raised when a django model object
    is not passed.
    """
    def __init__(self,obj: object):
        message = f"Object {type(obj)} is not of type models.Model"
        super().__init__(message)

class ModelHasNoFields(Exception):
    """
    raised when a django model object
    has no fields.
    """
    def __init__(self,model):
        message = f"Model {model} has no fields"
        super().__init__(message)