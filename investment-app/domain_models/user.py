from .portfolio import Portfolio

# PURPOSE: To allow for proper construction of the concept of a user in memory
class User:
    def __init__(self, id=None, *, login, balance, portfolios: dict[str, Portfolio] = None):
        self.id = id
        self.login = login
        self.balance = balance
        self.portfolios = portfolios if portfolios is not None else {}


    # INPUT: string representing portfolio name
    # OUTPUT: None
    # PRECONDITION: portfolio name is not in use and valid
    # POSTCONDITION: an empty portfolio is added with proper name to user account
    def add_portfolio(self, portfolio_name : str) -> None:
        self.portfolios[portfolio_name] = Portfolio(name = portfolio_name)


    # INPUT: string representing portfolio name
    # OUTPUT: None
    # PRECONDITION: portfolio name is in use
    # POSTCONDITION: the portfolio with matching name is removed from the user account
    def remove_portfolio(self, portfolio_name : str) -> None:
        del self.portfolios[portfolio_name]

    
    # INPUT: float representing amount of funds to add to balance
    # OUTPUT: None
    # PRECONDITION: funds to add is positive
    # POSTCONDITION: funds are properly added to user account balance
    def add_funds(self, funds_to_add : float) -> None:
        self.balance += funds_to_add


    # INPUT: float representing amount of funds to subtract from balance
    # OUTPUT: None
    # PRECONDITION: funds to sub is positive and <= balance
    # POSTCONDITION: funds are properly subtracted from user account balance
    def sub_funds(self, funds_to_sub : float) -> None:
        self.balance -= funds_to_sub






