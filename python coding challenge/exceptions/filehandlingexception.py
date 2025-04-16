class FileHandlingException(Exception):
    def __init__(self, message="Error accessing the file"):
        super().__init__(message)
