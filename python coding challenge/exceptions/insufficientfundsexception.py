class InsufficientFundsException(Exception):
    def __init__(self, message="Donation amount is below the minimum allowed ($10)"):
        super().__init__(message)
