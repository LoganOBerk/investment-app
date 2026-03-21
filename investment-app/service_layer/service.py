import sys
from persistence_layer import DatabaseError
from collections import defaultdict
from domain_models import *

# PURPOSE: To provide a wrapper for errors that propagate from service
class ServiceError(Exception):
    pass


# PURPOSE: To provide a central layer for domain model population and handle user requests 
class Service:
    def __init__(self, database):
        self.db = database


    # INPUT: tuple of two strings representing user credentials; login, password
    # OUTPUT: None
    # PRECONDITION: credentials passed basic validation
    # POSTCONDITION: a database call is made to attempt to update the database
    def create_account(self, credentials : tuple[str, str]) -> None:
        try:
        # TODO: Add user to the db
            pass
        except DatabaseError as e:
            raise ServiceError("Failed to create account") from e


    # INPUT: string representing user login
    # OUTPUT: User object
    # PRECONDITION: user has already entered valid credentials which exist in database
    # POSTCONDITION: a user object is created and an attempt is made to populate with database information
    def find_account(self, login : str) -> User:
        # TODO: Create user object
        try:
        # TODO: Populate user object
            pass
        except DatabaseError as e:
            raise ServiceError("Failed to find account") from e


    # INPUT: User, float representing funds requested
    # OUTPUT: None
    # PRECONDITION: funds requested must be positive
    # POSTCONDITION: an attempt is made to update the user funds in the database and then in memory funds are updated if successful
    def fund_account(self, user_account : User, funds_request : float) -> None:
        try:
        #TODO: update db funds
            pass
        except DatabaseError as e:
            raise ServiceError("Failed to update funds") from e

        user_account.add_funds(funds_request)
        

    # INPUT: User, string representing a portfolio name
    # OUTPUT: None
    # PRECONDITION: portfolio name does not exist with current user and is a valid name
    # POSTCONDITION: an attempt is made to insert new portfolio into the database if successful in memory user is given an empty named portfolio and id is assigned
    def create_portfolio(self, user_account : User, portfolio_name : str) -> None:
        try:

            p_id = self.db.insert_portfolio(user_account.id, portfolio_name)

        except DatabaseError as e:
            raise ServiceError("Failed to create portfolio") from e

        # TODO: add new empty portfolio to user_account object
        user_account.portfolios[portfolio_name].id = p_id


    # INPUT: User, string representing portfolio name
    # OUTPUT: None
    # PRECONDITION: user contains this portfolio
    # POSTCONDITION: portfolio removal from database is attempted, if successful in memory portfolio is removed
    def remove_portfolio(self, user_account : User, portfolio_name : str) -> None:
        try:
        #TODO: call remove function for removing portfolio from db
            pass
        except DatabaseError as e:
            raise ServiceError("Failed to remove portfolio") from e

        user_account.remove_portfolio(portfolio_name)


    # INPUT: User, Portfolio, tuple of string and int representing ticker, quantity
    # OUTPUT: None
    # PRECONDITION: user account and portfolio is properly populated in memory and the user has enough balance to buy
    # POSTCONDITION: an attempt to update or insert into the database is made if successful buy the shares in memory and if the stock is new update the in memory stock id
    def execute_buy(self, user_account : User, portfolio : Portfolio, shares_requested : tuple[str, int]) -> None:
        # TODO: call api to get stock price
        # TODO: subtract funds from user account
        
        ticker, quantity = shares_requested

        s_id = None

        try:

            if portfolio.has_stock(ticker):
                # TODO: update the db
                pass
            else:
                 s_id = self.db.insert_stock(portfolio.id, shares_requested)
        
        except DatabaseError as e:
            raise ServiceError("Failed to execute buy") from e

        portfolio.buy_shares(shares_requested)

        if s_id != None:
            portfolio.stocks[ticker].id = s_id
        

    # INPUT: User, Portfolio, tuple of string and int representing ticker, quantity
    # OUTPUT: None
    # PRECONDITION: user account and portfolio is properly populated in memory and the user has enough shares
    # POSTCONDITION: an attempt to update or remove from the database is made if successful sell the shares in memory
    def execute_sell(self, user_account : User, portfolio : Portfolio, shares_requested : tuple[str, int]) -> None:
        # TODO: call api to get stock price
        # TODO: add funds to user account
        
        ticker, quantity = shares_requested

        try:

            if portfolio.has_stock(ticker) and quantity == portfolio.stocks[ticker].quantity:
                # TODO: remove from the db
                pass
            else:
                # TODO: update the db
                pass

        except DatabaseError as e:
            raise ServiceError("Failed to execute sell") from e

        portfolio.sell_shares(shares_requested)


    # INPUT: tuple of two strings representing user credentials login, password
    # OUTPUT: bool representing a valid credential match
    # PRECONDITION: credentials provided pass basic validation
    # POSTCONDITION: an attempt is made to resolve credentials
    def credentials_match(self, credentials : tuple[str, str]) -> bool:
        try:

            u_id = self.db.resolve_credentials(credentials)

        except DatabaseError as e:
            raise ServiceError("Failed to match credentials") from e

        return u_id != None


    # INPUT: Portfolio 
    # OUTPUT: a list of dicts that have key string with value of either string or int representing ticker and quantity across entire portfolio
    # PRECONDITION: portfolio is populated and up to date in memory
    # POSTCONDITION: None
    def package_portfolio_data(self, portfolio : Portfolio) -> list[dict[str, str | int]]:
        packaged_data = []

        for stock in portfolio.stocks.values():
            packaged_data.append({"ticker": stock.ticker, "quantity": stock.quantity})

        return packaged_data


    # INPUT: string representing a user login
    # OUTPUT: a tuple that has tuple, list of tuples, list of tuples which represent all of the raw database data
    # PRECONDITION: user login exists
    # POSTCONDITION: an attempt to retrieve all database items related to user is made
    def retrieve_stored_data(self, login : str) -> tuple[tuple, list[tuple], list[tuple]]:
       
        stored_user = self.db.pull_user(login)
        stored_portfolios = self.db.pull_portfolios(stored_user[0])
        stored_stocks = self.db.pull_stocks(stored_user[0])

        return stored_user, stored_portfolios, stored_stocks


    # INPUT: list of tuples representing all users stocks
    # OUTPUT: a dict keyed by an int with a list of tuples, with the key being the pid and the tuples being the portfolios stock data
    # PRECONDITION: stored stocks contains all stock data related to user
    # POSTCONDITION: None
    def assign_portfolio_allocations(self, stored_stocks : list[tuple]) -> dict[int, list[tuple]]:
        portfolio_assignments = defaultdict(list)
        for stock in stored_stocks:
            p_id = stock[0]
            portfolio_assignments[p_id].append(stock[1:])

        return portfolio_assignments


    # INPUT: User and string representing login
    # OUTPUT: None
    # PRECONDITION: login exists in database
    # POSTCONDITION: in memory user account is populated
    def populate_user_account(self, user_account : User, login : str) -> None:
        stored_user, stored_portfolios, stored_stocks = self.retrieve_stored_data(login)

        user_account.id, user_account.login, user_account.balance = stored_user

        self.populate_user_portfolios(user_account.portfolios, stored_portfolios, stored_stocks)
        

    # INPUT: keyed dict of all user portfolios, list of all stored portfolio tuples, list of all stored stock tuples
    # OUTPUT: None
    # PRECONDITION: in memory user portfolios are empty, stored portfolios contains all database data related to user portfolios as does stored stocks
    # POSTCONDITION: in memory user account portfolios are all populated
    def populate_user_portfolios(self, user_portfolios : dict[str, Portfolio], stored_portfolios : list[tuple], stored_stocks : list[tuple]) -> None:
        stored_stocks = self.assign_portfolio_allocations(stored_stocks)

        for portfolio in stored_portfolios:

            p_id = portfolio[0]
            p_name = portfolio[1]

            user_portfolios[p_name] = Portfolio(id=p_id,name=p_name)

            self.populate_portfolio_stocks(user_portfolios[p_name].stocks, stored_stocks.get(p_id, []))
    

    # INPUT: a dict of all in memory portfolio stocks, a list of tuples of all stored stocks related to portfolio 
    # OUTPUT: None
    # PRECONDITION: stored portfolio stocks contain all stocks related to the current portfolio
    # POSTCONDITION: user portfolio is populated with its respective stocks
    def populate_portfolio_stocks(self, portfolio_stocks : dict[str, Stock], stored_portfolio_stocks : list[tuple]) -> None:

        for stock in stored_portfolio_stocks:

            s_id = stock[0]
            s_ticker = stock[1]
            s_quantity = stock[2]

            portfolio_stocks[s_ticker] = Stock(id=s_id, ticker=s_ticker, quantity=s_quantity)


    # INPUT: None
    # OUTPUT: None
    # PRECONDITION: Application is running
    # POSTCONDITION: Application is terminated
    @staticmethod
    def exit_app() -> None:
        sys.exit(0)