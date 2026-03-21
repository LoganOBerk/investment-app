from integration_layer import Api as api


# PURPOSE: To provide an abstraction layer that handles all validation to allow other layers to assume the happy path
class Validator:
    def __init__(self, service):
        self.serv = service


    # INPUT: tuple of two strings representing login, password 
    # OUTPUT: bool determining if user credentials are valid
    # PRECONDITION: None
    # POSTCONDITION: credentials have been validated
    def account_validator(self, credentials : tuple[str, str], new : bool) -> bool:
        # TODO: Validate account credentials using service method
        # TODO: Add any other validation you want, if you want to enforce certain additional constraints
        pass

     
    # INPUT: User, String, bool; string represents portfolio name, bool telling if a portfolio is being created or not
    # OUTPUT: bool determining if the portfolio is valid
    # PRECONDITION: The user is logged in and populated from database
    # POSTCONDITION: portfolio request has been validated
    @staticmethod
    def portfolio_validator(user_account, portfolio_name : str, create : bool) -> bool:
        # TODO: Validate that portfolio_name doesnt already exist
        # TODO: Add any other validation you want, AKA empty name insert
        # TODO: ensure creation only is allowed when portfolio doesnt exist and removal is only allowed when it does
        pass


    # INPUT: Portfolio, String, bool; string represents the stock ticker, and bool determines if this is a purchase or sale
    # OUTPUT: bool determining if ticker is valid
    # PRECONDITION: The user is logged in and populated from database
    # POSTCONDITION: stock ticker has been validated
    @staticmethod
    def stock_ticker_validator(portfolio, ticker : str, purchase : bool) -> bool:
        # TODO: Validate ticker symbol format with regex
        # TODO: identify if we are purchasing a stock or not
        # TODO: if stock is not being purchased check if it exists in the portfolio
        # TODO: if stock is being purchased find out if it exists in yfinance
        # TODO: if ticker doesnt exist in portfolio and we arent purchasing return false
        pass


    # INPUT: Portfolio, tuple of string and int, bool; tuple represented requested shares given ticker, quantity, bool represents if we are buying or selling
    # OUTPUT: bool determining if requested stock quantity is valid
    # PRECONDITION: stock ticker is a valid ticker for our operation
    # POSTCONDITION: stock quantity request has been validated
    @staticmethod
    def stock_quantity_validator(portfolio, shares_requested : tuple[str, int], purchase : bool) -> bool:
        # TODO: If we are not purchasing check if portfolio has enough shares of stock
        # TODO: (optional) if we are purchasing ensure the purchase amount is not more than number of avalible shares in open market
        pass


    # INPUT: float, tuple of string and int, bool; float represents the user balance, tuple is the stock, quantity request, bool is if we are buying or selling
    # OUTPUT: bool determining if user has sufficient balance
    # PRECONDITION: shares requested are valid
    # POSTCONDITION: user balance is validated
    @staticmethod
    def sufficient_balance_validator(balance : float, shares_requested : tuple[str, int], purchase : bool) -> bool:
        # TODO: get price of stock from api
        # TODO: Validate that the user has sufficient balance for the requested stock and amount
        # TODO: if user is selling we return true by default
        pass


    # INPUT: float, float; float reepresents user balance, float represents funds requested
    # OUTPUT: bool determining if funds request is valid
    # PRECONDITION: None
    # POSTCONDITION: funds request is accepted or denied
    @staticmethod
    def fund_validator(balance : float, funds_request : float) -> bool:
        # TODO: validate that the funds are positive and reasonable within discrecion
        pass