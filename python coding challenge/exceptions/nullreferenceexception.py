class NullReferenceException(Exception):
    def __init__(self, message="Missing information in pet details"):
        super().__init__(message)
