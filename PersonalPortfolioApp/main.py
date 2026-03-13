from database import Database
from service import Service
from validator import Validator
from cli import Cli

def init():
    db_source = 'dummy.db'

    db = Database(db_source)
    serv = Service(db)
    val = Validator(serv)
    cli = Cli(serv, val)

    cli.run()


if __name__ == "__main__" :
   init()
