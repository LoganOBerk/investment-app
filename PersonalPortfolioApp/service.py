import sys
from user import User
from portfolio import Portfolio
from stock import Stock
import user

class Service:
    
    def __init__(self, database):
        self.db = database

    def create_account(self, credentials : tuple) -> User:
        #TODO: Create empty user object
        #TODO: Add user to the db
        pass
    
    def find_account(self, credentials : tuple) -> User:
        u_id = self.get_user_id(credentials)
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
        r = portfolio.add_stock(stock_dat)
        

        if(r == "added"):
            #TODO: add to database 
            pass
        else:
            #TODO: update database
            pass
    
    def execute_sell(self, userAccount : User, portfolio : Portfolio, stock_dat : tuple) -> None:
        #TODO: call api to get stock price
        #TODO: add funds to user account
        #TODO: remove the stock(s) from the portfolio
        r = portfolio.remove_stock(stock_dat)


        if(r == "removed"):
            #TODO: remove from database
            pass
        else:
            #TODO: update database

            pass

    
    
    def get_user_id(self, credentials):
        key = credentials
        u_id = self.db.user_id_resolver(key)
      
        return u_id

    def get_portfolio_id(self, userAccount, portfolioName):
        u_id = self.convert_user_key(userAccount)
        key =  u_id , portfolioName
        p_id = self.db.portfolio_id_resolver(key)

        return p_id

    def get_stock_id(self, userAccount, portfolio, ticker):
        u_id, p_id = self.convert_portfolio_key(userAccount, portfolio)
        key = u_id, p_id, ticker
        s_id = self.db.stock_id_resolver(key)

        return s_id

    def user_exists(self, id_path):
        #TODO: identify if user id exists in db
        pass
    
    @staticmethod
    def exitApp():
        sys.exit(0)