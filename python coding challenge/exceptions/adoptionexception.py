class AdoptionException(Exception):
    def __init__(self, message="Adoption process failed"):
        super().__init__(message)
