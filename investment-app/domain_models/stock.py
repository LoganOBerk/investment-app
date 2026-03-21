# PURPOSE: To allow for proper construction of the concept of a stock in memory
class Stock:
    def __init__(self, id=None, *, ticker, quantity):
        self.id = id
        self.ticker = ticker
        self.quantity = quantity


    # INPUT: int representing the amount of stock we are adding
    # OUTPUT: None
    # PRECONDITION: amount to increment is positive
    # POSTCONDITION: Stock is properly updated to represent the proper quantity
    def increment_quantity(self, inc_amt : int) -> None:
        self.quantity += inc_amt


    # INPUT: int representing the amount of stock we are decrementing
    # OUTPUT: None
    # PRECONDITION: amount to decrement is positive and <= quantity
    # POSTCONDITION: Stock is properly updated to represent the proper quantity
    def decrement_quantity(self, dec_amt : int) -> None:
        self.quantity -= dec_amt