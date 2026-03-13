import sys
from user import User
from portfolio import Portfolio
from stock import Stock

class Service:
    
    def __init__(self, database):
        self.db = database

    def create_account(self, credentials : tuple) -> User:
        #TODO: Add user to the db
        #TODO: Create empty user object
        pass
    
    def find_account(self, credentials : tuple) -> User:
        #TODO: Pull user data from db
        #TODO: Create and Populate user object
        pass
    
    def create_portfolio(self, userAccount : User, portfolioName : str) -> None:
        #TODO: add new empty portfolio to userAccount object
        #TODO: ensure database updates
        pass
    
    def execute_buy(self, userAccount : User, portfolio : Portfolio, stock_dat : tuple) -> None:
        #TODO: call api to get stock price
        #TODO: subtract funds from user account
        #TODO: add the stock(s) to the portfolio
        pass
    
    def execute_sell(self, userAccount : User, portfolio : Portfolio, stock_dat : tuple) -> None:
        #TODO: call api to get stock price
        #TODO: add funds to user account
        #TODO: remove the stock(s) from the portfolio
        pass

    def populate_userAccount(self, userAccount : User) -> None:
        self.populate_portfolios(userAccount, userAccount.portfolios)

    def populate_portfolio(self, userAccount : User, portfolio : Portfolio) -> None:
        #TODO: Pull portfolio data from db with context
        #TODO: Populate portfolio with data
        self.populate_stocks(userAccount, portfolio, portfolio.stocks)

    def populate_stock(self, userAccount : User, portfolio : Portfolio, stock : Stock) -> None:
        #TODO: Pull stock data from db with context
        #TODO: Populate stock with data
        pass

    def populate_portfolios(self, userAccount: User, portfolios : dict[str, Portfolio]) -> None:
        for portfolio in portfolios.values():
            self.populate_portfolio(userAccount, portfolio)

    def populate_stocks(self, userAccount : User, portfolio : Portfolio, stocks : dict[str, Stock]) -> None:
        for stock in stocks.values():
            self.populate_stock(userAccount, portfolio, stock)
        

    @staticmethod
    def exitApp():
        sys.exit(0)