class InvalidPetAgeException(Exception):
    def __init__(self, message="Pet age must be a positive number"):
        super().__init__(message)
