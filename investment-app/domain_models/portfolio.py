from .stock import Stock

# PURPOSE: To allow for proper construction of the concept of a portfolio in memory
class Portfolio:
    def __init__(self, id=None, *, name, stocks: dict[str, Stock] = None):
        self.id = id
        self.name = name
        self.stocks = stocks if stocks is not None else {}


    # INPUT: string to indicate ticker symbol
    # OUTPUT: bool representing if the ticker exists in the portfolio
    # PRECONDITION: ticker string is a valid stock ticker
    # POSTCONDITION: None
    def has_stock(self, ticker : str) -> bool:
        return ticker in self.stocks


    # INPUT: tuple of requested shares; ticker, quantity
    # OUTPUT: None
    # PRECONDITION: requested shares are a valid request
    # POSTCONDITION: portfolio is properly updated based on the purchase amount
    def buy_shares(self, shares_requested : tuple[str, int]) -> None:

        t, q = shares_requested


        if (self.has_stock(t)):
            self.stocks[t].increment_quantity(q)
        else:
            self.stocks[t] = Stock(ticker=t, quantity=q)


    # INPUT: tuple of requested shares; ticker, quantity
    # OUTPUT: None
    # PRECONDITION: requested shares are a valid request
    # POSTCONDITION: portfolio is properly updated based on the sell amount
    def sell_shares(self, shares_requested : tuple[str, int]) -> None:

        t, q = shares_requested


        self.stocks[t].decrement_quantity(q)

        if (self.stocks[t].quantity == 0):
            del self.stocks[t]

