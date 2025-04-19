class ArtWorkNotFoundException(Exception):
    def __init__(self, message="Artwork not found"):
        super().__init__(message)
